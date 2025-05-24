resource "aws_lambda_function" "lambda" {
  function_name = local.lambda_function_full_name
  architectures = ["arm64"]
  package_type  = "Image"
  image_uri     = "061051222129.dkr.ecr.ap-northeast-1.amazonaws.com/lambda-bot-prod:latest" # this is a dummy image for now. image will be updated by github actions.
  role          = aws_iam_role.lambda_role.arn
  publish       = true

  memory_size = var.lambda_memory_size
  timeout     = var.lambda_timeout

  lifecycle {
    ignore_changes = [
      image_uri
    ]
  }

  environment {
    variables = merge(
      var.lambda_environment,
      local.lambda_env_vars
    )
  }

  tracing_config {
    mode = "Active"
  }

  depends_on = [
    aws_cloudwatch_log_group.lambda
  ]

  tags = {
    Name = local.lambda_function_full_name
  }
}