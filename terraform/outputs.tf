output "instance_public_ip" {
  value = aws_instance.task_manager_server.public_ip
}

output "instance_public_dns" {
  value = aws_instance.task_manager_server.public_dns
}