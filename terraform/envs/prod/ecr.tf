module "ecr" {
  source              = "../../modules/ecr"
  ecr_repository_name = "${var.lambda_function_name}-${var.env}"
}