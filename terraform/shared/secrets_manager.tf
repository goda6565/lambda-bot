module "gemini_api_key" {
  source = "../modules/secretsmanager"

  secret_manager_secrets_name = "gemini-api-key"
}