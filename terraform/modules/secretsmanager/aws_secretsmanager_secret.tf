resource "aws_secretsmanager_secret" "secretsmanager_secret" {
  name = var.secret_manager_secrets_name
}