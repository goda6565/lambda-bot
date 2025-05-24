output "secrets_manager_secrets_arn" {
  value = aws_secretsmanager_secret.secretsmanager_secret.arn
}