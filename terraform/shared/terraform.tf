terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.98.0"
    }
  }
  required_version = ">= 1.12.0"
  backend "s3" {
    bucket = "lambda-bot-tfstate-backend"
    key    = "shared"
    region = "ap-northeast-1"
  }
}