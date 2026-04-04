variable "aws_region" {
  default = "eu-north-1"
}

variable "instance_name" {
  default = "task-manager-tf"
}

variable "instance_type" {
  default = "t3.micro"
}

variable "ami_id" {
  description = "Ubuntu AMI ID"
  default     = "ami-0c1ac8a41498c1a9c"
}

variable "key_name" {
  description = "Existing AWS key pair name"
  default     = "task-key"
}