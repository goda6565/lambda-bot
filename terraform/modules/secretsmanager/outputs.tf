output "secrets_manager_secrets_arns" {
  value = aws_secretsmanager_secret.secretsmanager_secret.arn
}