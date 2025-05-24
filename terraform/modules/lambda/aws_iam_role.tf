resource "aws_iam_role" "lambda_role" {
  name               = "${local.lambda_function_full_name}-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}