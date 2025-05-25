variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-1"
}

variable "lambda_function_name" {
  description = "The name of the lambda function"
  type        = string
  default     = "lambda-bot"
}

variable "env" {
  description = "The environment of the lambda function"
  type        = string
  default     = "test"
}