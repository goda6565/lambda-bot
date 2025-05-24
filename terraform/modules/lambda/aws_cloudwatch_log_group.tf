resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/${local.lambda_function_full_name}"
  retention_in_days = var.cloudwatch_log_retention_in_days

  tags = {
    Name = "/aws/lambda/${local.lambda_function_full_name}"
  }
}