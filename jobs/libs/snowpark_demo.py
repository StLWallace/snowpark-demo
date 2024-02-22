from snowflake.snowpark import DataFrame, functions as F


def transform_source_table(source_table: DataFrame) -> DataFrame:
    """A basic transformation to test this out"""
    agg_table = source_table.group_by(F.col("AIQ_INDID")).agg(
        F.mean("AIQ_HOME_AGE").alias("mean_home_age"),
        F.mean("HOMEVALUEIQ").alias("mean_home_value_iq"),
    )

    return agg_table
