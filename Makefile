# terraform
.PHONY: tf-fmt
tf-fmt:
	cd terraform && terraform fmt -recursive

# check
.PHONY: check
check:
	uv run isort .
	uvx ruff@latest check app . --fix
	uvx ruff@latest format app .
	uv run pyright