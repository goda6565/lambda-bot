resource "aws_lambda_function" "lambda" {
  function_name = local.lambda_function_full_name
  architectures = ["arm64"]
  package_type  = "Image"
  image_uri     = "public.ecr.aws/lambda/python:3.12" # this is a dummy image for now. image will be updated by github actions.
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
    variables = var.lambda_environment
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