resource "aws_lambda_alias" "lambda" {
  name             = var.env
  function_name    = aws_lambda_function.lambda.function_name
  function_version = aws_lambda_function.lambda.version

  lifecycle {
    ignore_changes = [
      function_version
    ]
  }
}