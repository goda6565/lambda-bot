resource "aws_secretsmanager_secret_version" "secretmanager_secret_version" {
  secret_id     = aws_secretsmanager_secret.secretsmanager_secret.id
  secret_string = "dummy"

  lifecycle {
    ignore_changes = [
      secret_string
    ]
  }
}