output "instance_ids" { value = aws_instance.main[*].id }
output "public_ips" { value = aws_instance.main[*].public_ip }
output "private_ips" { value = aws_instance.main[*].private_ip }
output "security_group_id" { value = aws_security_group.ec2.id }
