output "input_bucket_name" {
  value = aws_s3_bucket.input.id
}

output "output_bucket_name" {
  value = aws_s3_bucket.output.id
}

output "lambda_arn" {
  value = aws_lambda_function.nova_agent.arn
}
