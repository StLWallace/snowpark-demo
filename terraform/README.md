<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_snowflake"></a> [snowflake](#requirement\_snowflake) | 0.86.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_snowflake"></a> [snowflake](#provider\_snowflake) | 0.86.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [snowflake_procedure.sdoh](https://registry.terraform.io/providers/Snowflake-Labs/snowflake/0.86.0/docs/resources/procedure) | resource |
| [snowflake_database.test](https://registry.terraform.io/providers/Snowflake-Labs/snowflake/0.86.0/docs/data-sources/database) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_account"></a> [account](#input\_account) | Snowflake account name | `string` | n/a | yes |
| <a name="input_authenticator"></a> [authenticator](#input\_authenticator) | If using SAML, value should be 'externalbrowser' | `string` | n/a | yes |
| <a name="input_environment"></a> [environment](#input\_environment) | The environment where resources will be deployed | `string` | n/a | yes |
| <a name="input_libraries_stage_name"></a> [libraries\_stage\_name](#input\_libraries\_stage\_name) | Internal stage that stores custom Python libraries | `string` | n/a | yes |
| <a name="input_private_key"></a> [private\_key](#input\_private\_key) | Snowflake private key value | `string` | n/a | yes |
| <a name="input_schema_name"></a> [schema\_name](#input\_schema\_name) | Name of target schema where stuff lives. | `string` | n/a | yes |
| <a name="input_user"></a> [user](#input\_user) | Snowflake username | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END_TF_DOCS -->
