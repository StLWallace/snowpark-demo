variable "environment" {
  description = "The environment where resources will be deployed"
  type        = string
}

variable "schema_name" {
  description = "Name of target schema where stuff lives."
  type        = string
}

variable "libraries_stage_name" {
  description = "Internal stage that stores custom Python libraries"
  type        = string
}

variable "account" {
  description = "Snowflake account name"
  type        = string
}

variable "authenticator" {
  description = "If using SAML, value should be 'externalbrowser'"
  type        = string
}

variable "private_key" {
  description = "Snowflake private key value"
  type        = string
}

variable "user" {
  description = "Snowflake username"
  type        = string
}
