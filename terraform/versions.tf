terraform {
  required_providers {
    snowflake = {
      source  = "Snowflake-Labs/snowflake"
      version = "0.86.0"
    }
  }
}

provider "snowflake" {
  account       = var.account
  authenticator = var.authenticator
}
