module "api_gateway" {
  source                  = "../../modules/api_gateway"
  env                     = var.env
  lambda_function_name    = var.lambda_function_name
  lambda_alias_name       = module.lambda.aws_lambda_alias_name
  lambda_alias_invoke_arn = module.lambda.aws_lambda_alias_invoke_arn
}