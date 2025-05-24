module "slack_bot_token" {
  source = "../../modules/secretsmanager"

  secret_manager_secrets_name = "slack-bot-token-dev"
}

module "slack_signing_secret" {
  source = "../../modules/secretsmanager"

  secret_manager_secrets_name = "slack-signing-secret-dev"
}

module "gemini_api_key" {
  source = "../../modules/secretsmanager"

  secret_manager_secrets_name = "gemini-api-key-dev"
}