from snowflake.snowpark import Session, Table, DataFrame
from snowflake.snowpark import functions as F
from libs.utils import get_connection_params


CONF_PATH = "../conf/snowflake_conn.yml"
SOURCE_DB_NAME = "AIQ_BUSINESS_DATA_SAMPLES_SNOWFLAKE_SECURE_SHARE_1638885213840"
SOURCE_SCHEMA_NAME = "PUBLIC"
SOURCE_TABLE_NAME = "SDOH_SAMPLE"

TARGET_DB_NAME = "TEST_DB"
TARGET_SCHEMA_NAME = "SNOWPARK_DEMO"


def transform_source_table(source_table: DataFrame) -> DataFrame:
    """A basic transformation to test this out"""
    agg_table = source_table.group_by(F.col("AIQ_INDID")).agg(
        F.mean("AIQ_HOME_AGE").alias("mean_home_age"),
        F.mean("HOMEVALUEIQ").alias("mean_home_value_iq"),
    )

    return agg_table


def main(session: Session):
    """"""
    source_table_fullname = f"{SOURCE_DB_NAME}.{SOURCE_SCHEMA_NAME}.{SOURCE_TABLE_NAME}"
    target_table_fullname = f"{TARGET_DB_NAME}.{TARGET_SCHEMA_NAME}.sdoh_agg"
    sdoh_sample = session.table(source_table_fullname)

    agg_table = transform_source_table(source_table=sdoh_sample)

    agg_table.write.mode("overwrite").save_as_table(target_table_fullname)


if __name__ == "__main__":
    connection_params = get_connection_params(CONF_PATH)
    session = Session.builder.configs(
        connection_params.model_dump(exclude_none=True, by_alias=True)
    ).create()

    main(session=session)
