resource "aws_iam_role_policy_attachment" "github_actions_oidc_role_policy_attachment" {
  role       = aws_iam_role.github_actions_oidc_role.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess" # TODO: 必要最低限のポリシーに変更する
}