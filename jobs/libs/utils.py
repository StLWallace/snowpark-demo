import yaml
from models.snowflake import SnowflakeConnectionParameters


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
