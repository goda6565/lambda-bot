module "bootstrap" {
  source = "../modules/bootstrap"

  github_actions_oidc_role_name = "github-actions-oidc-role"
  github_organization           = "goda6565"
  github_repository             = "lambda-bot"
}