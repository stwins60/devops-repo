resource "aws_db_instance" "postgres" {
  identifier           = var.db_identifier
  engine              = "postgres"
  engine_version      = "15.3"
  instance_class      = var.instance_class
  allocated_storage   = 20
  storage_type        = "gp3"
  
  db_name  = var.database_name
  username = var.db_username
  password = var.db_password
  
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name
  
  backup_retention_period = 7
  skip_final_snapshot    = true
  
  tags = {
    Name = var.db_identifier
  }
}

resource "aws_db_subnet_group" "main" {
  name       = "${var.db_identifier}-subnet-group"
  subnet_ids = var.subnet_ids
  
  tags = {
    Name = "${var.db_identifier}-subnet-group"
  }
}

resource "aws_security_group" "rds" {
  name        = "${var.db_identifier}-sg"
  description = "Security group for RDS"
  vpc_id      = var.vpc_id
  
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }
}
