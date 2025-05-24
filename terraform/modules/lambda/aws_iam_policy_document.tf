data "aws_iam_policy_document" "lambda_policy_document" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

data "aws_iam_policy_document" "lambda_secret_manager_policy_document" {
  statement {
    effect = "Allow"

    actions   = ["secretsmanager:GetSecretValue"]
    resources = [for s in values(var.secret_manager_secrets) : s.arn]
  }
}