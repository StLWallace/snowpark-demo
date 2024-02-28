from snowflake.snowpark import Session
from libs.utils import get_connection_params, insert_overwrite
from tables.sdoh_agg import SdohAgg, SdohSemantic


CONF_PATH = "../conf/snowflake_conn.yml"
SOURCE_DB_NAME = "AIQ_BUSINESS_DATA_SAMPLES_SNOWFLAKE_SECURE_SHARE_1638885213840"
SOURCE_SCHEMA_NAME = "PUBLIC"
SOURCE_TABLE_NAME = "SDOH_SAMPLE"

TARGET_DB_NAME = "TEST_DB"
TARGET_SCHEMA_NAME = "SNOWPARK_DEMO"

PARTITION_COL = "loaded_date"
PARTITION_VAL = "20240102"


def process(session: Session):
    """Loads a source table, performs some basic transformations, then writes to a table

    If the target table doesn't exist, it will create it.
    """
    source_table_fullname = f"{SOURCE_DB_NAME}.{SOURCE_SCHEMA_NAME}.{SOURCE_TABLE_NAME}"
    target_table_fullname = f"{TARGET_DB_NAME}.{TARGET_SCHEMA_NAME}.sdoh_agg"
    sdoh_sample = session.table(source_table_fullname)

    sdoh_agg = SdohAgg(session=session, sdoh_sample=sdoh_sample)
    sdoh_semantic = SdohSemantic(session=session, sdoh_agg=sdoh_agg)

    insert_overwrite(
        session=session,
        target_table_name=target_table_fullname,
        new_data=sdoh_agg,
        partition_col=PARTITION_COL,
        partition_val=PARTITION_VAL,
    )


if __name__ == "__main__":
    connection_params = get_connection_params(CONF_PATH)
    session = Session.builder.configs(
        connection_params.model_dump(exclude_none=True, by_alias=True)
    ).create()

    process(session=session)
