""""""
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Literal


class SnowflakeConnectionParameters(BaseModel):
    """Attributes for creating Snowflake connection"""

    model_config = ConfigDict(populate_by_name=True)
    account: str = Field(alias="ACCOUNT")
    user: str = Field(alias="USER")
    password: Optional[str] = Field(None, alias="PASSWORD")
    role: Optional[str] = Field(None, alias="ROLE")
    warehouse: Optional[str] = Field(None, alias="WAREHOUSE")
    database: Optional[str] = Field(None, alias="DATABASE")
    db_schema: Optional[str] = Field(None, alias="SCHEMA")
    authenticator: Optional[Literal[None, "externalbrowser"]] = Field(
        None, alias="AUTHENTICATOR"
    )
