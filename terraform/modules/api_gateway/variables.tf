variable "env" {
  description = "The environment of the lambda function"
  type        = string
}

variable "lambda_function_name" {
  description = "The name of the lambda function"
  type        = string
}

variable "lambda_alias_invoke_arn" {
  description = "The invoke ARN of the lambda alias"
  type        = string
}

variable "lambda_alias_name" {
  description = "The name of the lambda alias"
  type        = string
}

variable "lambda_integration_timeout_milliseconds" {
  description = "The timeout milliseconds of the lambda integration"
  type        = number
  default     = 30000
}

variable "cloudwatch_log_retention_in_days" {
  description = "The retention period for the CloudWatch log group"
  type        = number
  default     = 30
}