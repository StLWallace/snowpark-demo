#!/bin/bash
# Zips a given Python library and uploads it to a named internal Snowflake Stage
# The library can be imported in the Snowflake console, stored procedures, and functions
# Args:
# - LIBS_PATH: local path to Python libraries
# - DB_NAME: name of Snowflake database containing stage
# - SCHEMA_NAME: name of Snowflake schema containing stage
# - STAGE_NAME: name of stage to upload files
PKG_DIR=jobs
DB_NAME=TEST_DB
SCHEMA_NAME=SNOWPARK_DEMO
STAGE_NAME=PYTHON_LIBS

zip -r jobs.zip $PKG_DIR

snow sql --query "put file://./jobs.zip '@$DB_NAME.$SCHEMA_NAME.$STAGE_NAME/snowpark_demo' OVERWRITE=TRUE"

rm jobs.zip
