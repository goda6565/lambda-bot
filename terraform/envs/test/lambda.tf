module "lambda" {
  source               = "../../modules/lambda"
  env                  = var.env
  lambda_function_name = var.lambda_function_name
  lambda_environment = {
    ENV = var.env
  }
  secret_manager_secrets_arns = [
    module.slack_bot_token.secrets_manager_secrets_arn,
    module.slack_signing_secret.secrets_manager_secrets_arn,
    module.gemini_api_key.secrets_manager_secrets_arn,
  ]
}