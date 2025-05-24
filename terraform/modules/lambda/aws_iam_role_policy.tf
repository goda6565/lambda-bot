resource "aws_iam_role_policy" "lambda_secret_manager_policy" {
  name   = "${local.lambda_function_full_name}-secret-manager-policy"
  role   = aws_iam_role.lambda_role.id
  policy = data.aws_iam_policy_document.lambda_secret_manager_policy_document.json
}
