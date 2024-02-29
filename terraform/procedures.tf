locals {
  full_stage_name = "@${data.snowflake_database.test.name}.${var.schema_name}.${var.libraries_stage_name}"
}

# Zip source code and upload it to stage


resource "snowflake_procedure" "sdoh" {
  name                = "sdoh-${var.environment}"
  database            = data.snowflake_database.test.name
  schema              = var.schema_name
  language            = "PYTHON"
  runtime_version     = "3.11"
  comment             = "Demo data process using sdoh data."
  return_type         = "VARCHAR"
  execute_as          = "CALLER"
  null_input_behavior = "RETURNS NULL ON NULL INPUT"
  handler             = "main"
  packages            = ["pydantic"]
  imports             = ["${local.full_stage_name}/snowpark-demo/jobs.zip"]
  statement           = <<EOT
import snowflake.snowpark as snowpark
from snowpark_demo.main import process


def main(session: snowpark.Session):
    process(session=session)
    return "This worked"
EOT
}
