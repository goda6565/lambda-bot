module "lambda" {
  source               = "../../modules/lambda"
  env                  = var.env
  lambda_function_name = var.lambda_function_name
  lambda_environment = {
    ENV = var.env
  }
  secret_manager_secrets_arns = [
    module.secrets_manager.slack_bot_token_arn,
    module.secrets_manager.slack_signing_secret_arn,
  ]
}