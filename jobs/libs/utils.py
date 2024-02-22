import yaml
from models.snowflake import SnowflakeConnectionParameters
from snowflake.snowpark import Session, DataFrame
from snowflake.snowpark.exceptions import SnowparkSQLException
import logging
import sys


def get_logger() -> logging.Logger:
    """Gets a logger and sets level to INFO"""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger


logger = get_logger()


def get_connection_params(conf_path: str) -> SnowflakeConnectionParameters:
    """Reads in yaml with Snowflake connection params

    Args:
        - conf_path: location of yaml containing Snowflake connection params

    Returns:
        - a BaseModel with config params from the yaml
    """
    with open(conf_path, "r") as f:
        conf_dict = yaml.safe_load(f)

    conf = SnowflakeConnectionParameters(**conf_dict)

    return conf


class SnowflakeTransaction:
    """Mimics a SQLAlchemy context manager
    Taken from https://github.com/snowflakedb/snowpark-python/issues/773
    """

    def __init__(
        self,
        session: Session,
    ):
        self.session = session
        self.actioned = False

    def __enter__(self):
        """Begin a transaction when context is opened"""
        self.session.sql("begin transaction").collect()
        return self

    def commit(self):
        self.session.sql("commit").collect()
        self.actioned = True

    def rollback(self):
        self.session.sql("rollback").collect()
        self.actioned = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if we already actioned, don't do anything
        if not self.actioned:
            # if an error was thrown, rollback
            if exc_type is not None:
                self.rollback()
            else:
                self.commit()


def insert_overwrite(
    session: Session,
    target_table_name: str,
    new_data: DataFrame,
    partition_col: str,
    partition_val: str,
) -> None:
    """Atomically deletes a logical partition of a table (if it exists) and inserts new data

    Because Snowflake stores data as (mostly) unconfigurable micropartitions, it's recommended to cluster your table by the logical partition value

    Args:
        - session: an active snowpark session
        - target_table_name: the table to be loaded
        - new_data: a DataFrame containing the new rows
        - partition_col: name of the column containing the logical partition value
        - partition_val: the logical partition value
    """
    try:
        # If table exists, delete target partition and reload
        with SnowflakeTransaction(session):
            target_table = session.table(target_table_name)
            delete_result = target_table.delete(
                target_table[partition_col] == partition_val
            )
            logger.info(delete_result)
            new_data.write.mode("append").save_as_table(table_name=target_table_name)

    except SnowparkSQLException:
        logger.info(f"Table {target_table_name} doesn't exist. Creating:")
        # If table doesn't exist, create it and cluster by partition_col
        new_data.write.mode("overwrite").save_as_table(
            table_name=target_table_name, clustering_keys=[partition_col]
        )
        logger.info(f"Table {target_table_name} created and loaded.")
