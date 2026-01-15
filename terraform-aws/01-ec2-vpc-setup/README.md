# EC2 Instance with VPC

Complete EC2 setup with VPC, subnets, and security groups.

## Resources Created

- VPC with CIDR block
- Public and private subnets
- Internet Gateway
- Route tables
- Security groups
- EC2 instance

## Project Structure

```
01-ec2-vpc-setup/
├── main.tf
├── variables.tf
├── outputs.tf
├── vpc.tf
├── security-groups.tf
├── terraform.tfvars.example
└── README.md
```

## Usage

```bash
# Initialize
terraform init

# Plan
terraform plan

# Apply
terraform apply

# Destroy
terraform destroy
```

## Variables

- `region` - AWS region
- `instance_type` - EC2 instance type
- `ami_id` - AMI ID for EC2
