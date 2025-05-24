module "slack_bot_token" {
  source = "../../modules/secretsmanager"

  secret_manager_secrets_name = "slack-bot-token"
}

module "slack_signing_secret" {
  source = "../../modules/secretsmanager"

  secret_manager_secrets_name = "slack-signing-secret"
}