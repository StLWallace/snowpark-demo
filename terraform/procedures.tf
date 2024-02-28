locals {
  full_stage_name = "@${data.snowflake_database.test.name}.${var.schema_name}.${var.libaries_stage_name}"
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
  return_behavior     = "IMMUTABLE"
  null_input_behavior = "RETURNS NULL ON NULL INPUT"
  handler             = "process"
  imports             = ["${local.full_stage_name}/snowpark-demo/jobs.zip"]
  statement           = <<EOT
  from jobs.main import process
EOT
}
