module "secrets_manager" {
  source = "../../modules/secretsmanager"

  secret_manager_secrets_names = [
    "slack-bot-token",
    "slack-signing-secret",
  ]
}