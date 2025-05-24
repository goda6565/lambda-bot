module "lambda" {
  source               = "../../modules/lambda"
  env                  = var.env
  lambda_function_name = var.lambda_function_name
  lambda_environment = {
    ENV = var.env
  }
}