resource "aws_secretsmanager_secret_version" "secretmanager_secret_version" {
  for_each = toset(var.secret_manager_secrets_names)

  secret_id     = aws_secretsmanager_secret.secretsmanager_secret[each.value].id
  secret_string = "dummy"

  lifecycle {
    ignore_changes = [
      secret_string
    ]
  }
}