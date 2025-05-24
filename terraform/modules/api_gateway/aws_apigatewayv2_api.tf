resource "aws_apigatewayv2_api" "lambda_api" {
  name          = "${local.lambda_function_full_name}-api"
  protocol_type = "HTTP"
}