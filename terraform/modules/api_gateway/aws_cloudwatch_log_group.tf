resource "aws_cloudwatch_log_group" "api_gateway" {
  name              = "/aws/lambda/${local.lambda_function_full_name}-api-gateway"
  retention_in_days = var.cloudwatch_log_retention_in_days

  tags = {
    Name = "/aws/lambda/${local.lambda_function_full_name}-api-gateway"
  }
}