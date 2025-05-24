resource "aws_secretsmanager_secret" "secretsmanager_secret" {
  for_each = toset(var.secret_manager_secrets_names)
  name     = each.value
}