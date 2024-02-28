from snowflake.snowpark import Session, DataFrame, functions as F

PARTITION_COL = "loaded_date"
PARTITION_VAL = "20240102"


class SdohAgg(DataFrame):
    """Creates an aggregated view of the sdoh_sample table"""

    def __init__(self, session: Session, sdoh_sample: DataFrame) -> None:
        """
        Args:
            - session: a snowpark Session object
            - sdoh_sample: a DataFrame or Table of the sdoh_sample data
        """
        table = self.create(sdoh_sample=sdoh_sample)
        super().__init__(session=session, plan=table._plan)

    def create(self, sdoh_sample: DataFrame) -> DataFrame:
        """Contains the steps for the exposed DataFrame that will be written or used in subsequent steps
        Args:
            - sdoh_sample: a Snowpark DataFrame (or Table) referencing the sdoh_sample source table

        Returns:
            - a DataFrame with transformations applied

        """
        agg_table = (
            sdoh_sample.group_by(F.col("AIQ_INDID"))
            .agg(
                F.mean("AIQ_HOME_AGE").alias("mean_home_age"),
                F.mean("HOMEVALUEIQ").alias("mean_home_value_iq"),
            )
            .with_column(PARTITION_COL, F.lit(PARTITION_VAL))
        )

        return agg_table


class SdohSemantic(DataFrame):
    """Creates a (fake, contrived) semantic table from the SDOH data"""

    def __init__(self, session: Session, sdoh_agg: SdohAgg) -> None:
        """Initializes an SdohSemantic DataFrame from its source tables

        Args:
            - session: a snowpark Session object
            - sdoh_agg: an initialized SdohAgg object
        """
        table = self.create(sdoh_agg=sdoh_agg)
        super().__init__(session=session, plan=table._plan)

    def create(self, sdoh_agg: SdohAgg) -> DataFrame:
        """Contains the steps for the exposed DataFrame that will be written or used in subsequent steps
        Args:
            - sdoh_agg: an initialized SdohAgg object

        Returns:
            - a DataFrame with transformations applied

        """
        semantic_table = sdoh_agg.filter(F.col("AIQ_HOME_AGE") > 0)

        return semantic_table
