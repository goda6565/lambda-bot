locals {
  lambda_function_full_name = "${var.lambda_function_name}-${var.env}"
}

locals {
  lambda_env_vars = {
    for key, value in var.secret_manager_secrets :
    "${upper(key)}_ARN" => value.arn
  }
}