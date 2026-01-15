variable "project_name" { type = string }
variable "environment" { type = string }
variable "vpc_id" { type = string }
variable "public_subnet_ids" { type = list(string) }
variable "private_subnet_ids" { type = list(string) }
variable "instance_type" { type = string }
variable "instance_count" { type = number }
variable "key_name" { type = string }
variable "tags" { type = map(string); default = {} }
