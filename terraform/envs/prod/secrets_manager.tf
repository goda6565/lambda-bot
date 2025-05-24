module "secrets_manager" {
  source = "../../modules/secretsmanager"

  secret_manager_secrets_name = "slack-bot-token"
}

module "secrets_manager" {
  source = "../../modules/secretsmanager"

  secret_manager_secrets_name = "slack-signing-secret"
}