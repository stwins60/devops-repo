# Terraform AWS Infrastructure

Infrastructure as Code (IaC) for provisioning AWS resources using Terraform. This configuration creates a complete AWS infrastructure including VPC, EC2 instances, S3 buckets, and RDS databases.

## 📋 Features

- VPC with public and private subnets
- EC2 instances with security groups
- S3 buckets for storage
- RDS database instances
- Application Load Balancer
- Auto Scaling Groups
- CloudWatch monitoring
- Modular architecture

## 🏗️ Project Structure

```
terraform-aws/
├── main.tf                    # Main configuration
├── variables.tf               # Variable definitions
├── outputs.tf                 # Output values
├── terraform.tfvars.example   # Example variables file
├── provider.tf                # Provider configuration
├── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── ec2/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── s3/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── rds/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── environments/
│   ├── dev/
│   │   └── terraform.tfvars
│   ├── staging/
│   │   └── terraform.tfvars
│   └── prod/
│       └── terraform.tfvars
├── scripts/
│   ├── init.sh
│   ├── plan.sh
│   ├── apply.sh
│   └── destroy.sh
└── README.md
```

## 🚀 Prerequisites

- Terraform 1.0 or higher
- AWS CLI configured with appropriate credentials
- AWS account with necessary permissions
- Basic understanding of AWS services

## 📦 Installation

1. **Install Terraform:**
```bash
# macOS
brew install terraform

# Linux
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```

2. **Configure AWS CLI:**
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter your default region (e.g., us-east-1)
# Enter your default output format (e.g., json)
```

3. **Clone and setup:**
```bash
cd terraform-aws
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your values
```

## ⚙️ Configuration

### terraform.tfvars

Create a `terraform.tfvars` file with your configuration:

```hcl
aws_region = "us-east-1"
environment = "dev"
project_name = "devops-demo"

vpc_cidr = "10.0.0.0/16"
availability_zones = ["us-east-1a", "us-east-1b"]

instance_type = "t3.micro"
instance_count = 2

db_instance_class = "db.t3.micro"
db_name = "devopsdb"
db_username = "admin"
db_password = "YourSecurePassword123!"

s3_bucket_name = "devops-demo-bucket"
```

## 🏃 Usage

### Initialize Terraform

```bash
terraform init
```

### Validate Configuration

```bash
terraform validate
```

### Plan Infrastructure

```bash
terraform plan
```

### Apply Configuration

```bash
terraform apply
# Review the plan and type 'yes' to confirm
```

### Destroy Infrastructure

```bash
terraform destroy
# Type 'yes' to confirm destruction
```

## 📝 Using Scripts

Convenience scripts are provided in the `scripts/` directory:

```bash
# Initialize
./scripts/init.sh

# Plan changes
./scripts/plan.sh dev

# Apply changes
./scripts/apply.sh dev

# Destroy infrastructure
./scripts/destroy.sh dev
```

## 🌍 Environments

The configuration supports multiple environments:

- **Development:** `environments/dev/`
- **Staging:** `environments/staging/`
- **Production:** `environments/prod/`

To use a specific environment:

```bash
terraform workspace new dev
terraform workspace select dev
terraform apply -var-file="environments/dev/terraform.tfvars"
```

## 📊 Resources Created

### VPC Module
- VPC with custom CIDR block
- Public and private subnets
- Internet Gateway
- NAT Gateway
- Route tables

### EC2 Module
- EC2 instances
- Security groups
- Key pairs
- Elastic IPs

### S3 Module
- S3 buckets
- Bucket policies
- Versioning
- Encryption

### RDS Module
- RDS database instances
- DB subnet groups
- Security groups
- Parameter groups

## 🔒 Security Best Practices

1. **Never commit sensitive data:**
   - Add `terraform.tfvars` to `.gitignore`
   - Use AWS Secrets Manager for sensitive values
   - Enable encryption for S3 and RDS

2. **Use IAM roles:**
   - Assign minimal required permissions
   - Use instance profiles for EC2

3. **Enable logging:**
   - CloudWatch logs
   - VPC Flow Logs
   - S3 access logs

## 📈 Monitoring

CloudWatch dashboards and alarms are automatically created for:
- EC2 CPU utilization
- RDS connections
- S3 bucket metrics
- Network traffic

## 🔄 State Management

### Remote State (Recommended)

Configure S3 backend for state storage:

```hcl
terraform {
  backend "s3" {
    bucket = "terraform-state-bucket"
    key    = "devops-demo/terraform.tfstate"
    region = "us-east-1"
    encrypt = true
    dynamodb_table = "terraform-locks"
  }
}
```

## 🧪 Testing

```bash
# Validate syntax
terraform fmt -check

# Validate configuration
terraform validate

# Security scanning
tfsec .

# Cost estimation
terraform plan -out=plan.tfplan
terraform show -json plan.tfplan | infracost breakdown --path -
```

## 📚 Additional Resources

- [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Terraform Best Practices](https://www.terraform-best-practices.com/)

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Run `terraform fmt` and `terraform validate`
4. Submit a pull request

## 📄 License

This project is for educational purposes.
