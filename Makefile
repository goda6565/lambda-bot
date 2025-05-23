# terraform
.PHONY: tf-fmt
tf-fmt:
	cd terraform && terraform fmt -recursive