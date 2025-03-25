packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = ">= 1.0.0"
    }
  }
}

variable "aws_region" {
  default = "us-east-1"
}

source "amazon-ebs" "ubuntu" {
  region         = var.aws_region
  source_ami     = "ami-012485deee5681dc0" # Updated to Ubuntu 22.04 AMI
  instance_type  = "t2.micro"
  ssh_username   = "ubuntu"
  ami_name       = "bakery-foundation-python39-${formatdate("YYYYMMDD-HHmmss", timestamp())}"
}

build {
  sources = ["source.amazon-ebs.ubuntu"]

  provisioner "shell" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y software-properties-common",
      "sudo add-apt-repository -y ppa:deadsnakes/ppa",
      "sudo apt-get update",
      "sudo apt-get install -y python3.9 python3.9-venv python3.9-dev",
      "python3.9 --version"
    ]
  }
}
