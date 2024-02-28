variable "environment" {
  description = "The environment where resources will be deployed"
  type        = string
}

variable "schema_name" {
  description = "Name of target schema where stuff lives."
  type        = string
}

variable "libaries_stage_name" {
  description = "Internal stage that stores custom Python libraries"
  type        = string
}
