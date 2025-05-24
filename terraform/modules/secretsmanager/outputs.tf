output "secrets" {
  value = {
    for k, v in aws_secretsmanager_secret.secretsmanager_secret :
    k => v.arn
  }
}