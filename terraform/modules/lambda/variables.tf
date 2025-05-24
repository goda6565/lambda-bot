variable "env" {
  description = "The environment of the lambda function"
  type        = string
}

variable "lambda_function_name" {
  description = "The name of the lambda function"
  type        = string
}

variable "lambda_memory_size" {
  description = "The memory size of the lambda function (MB)"
  type        = number
  default     = 128
}

variable "lambda_timeout" {
  description = "The timeout of the lambda function (seconds)"
  type        = number
  default     = 300
}

variable "lambda_environment" {
  description = "The environment variables of the lambda function"
  type        = map(string)
}

variable "cloudwatch_log_retention_in_days" {
  description = "The retention period for the CloudWatch log group"
  type        = number
  default     = 30
}

variable "secret_manager_secrets_arns" {
  description = "The arns of the secrets to be used by the lambda function"
  type        = list(string)
}