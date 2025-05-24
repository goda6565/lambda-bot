resource "aws_apigatewayv2_route" "lambda_function_route" {
  api_id    = aws_apigatewayv2_api.lambda_api.id
  route_key = "POST /invoke"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}
