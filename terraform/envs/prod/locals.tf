locals {
  secret_manager_secrets = {
    for k, v in module.secrets_manager.secrets :
    k => {
      arn = v
    }
  }
}