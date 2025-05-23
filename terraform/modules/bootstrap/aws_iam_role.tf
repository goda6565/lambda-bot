resource "aws_iam_role" "github_actions_oidc_role" {
  name               = var.github_actions_oidc_role_name
  assume_role_policy = data.aws_iam_policy_document.github_actions_oidc_policy_document.json
}