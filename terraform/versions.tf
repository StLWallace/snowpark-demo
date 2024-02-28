terraform {
  required_providers {
    snowflake = {
      source  = "Snowflake-Labs/snowflake"
      version = "0.86.0"
    }
  }
}

provider "snowflake" {
  profile = "default"
}
