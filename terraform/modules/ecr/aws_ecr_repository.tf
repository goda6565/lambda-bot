resource "aws_ecr_repository" "ecr_repository" {
  name                 = var.ecr_repository_name
  image_tag_mutability = "IMMUTABLE"

  tags = {
    Name = var.ecr_repository_name
  }

  image_scanning_configuration {
    scan_on_push = true
  }
}