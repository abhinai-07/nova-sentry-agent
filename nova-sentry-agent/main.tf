provider "aws" {
  region = "us-east-1"
}

# Unique naming
resource "random_id" "hex" { byte_length = 4 }

# S3 Buckets
resource "aws_s3_bucket" "input" { bucket = "nova-input-${random_id.hex.hex}" }
resource "aws_s3_bucket" "output" { bucket = "nova-output-${random_id.hex.hex}" }

# IAM Role for the Nova Agent
resource "aws_iam_role" "nova_role" {
  name = "NovaGuardAgentRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

# Permissions for Nova, Comprehend, and S3
resource "aws_iam_role_policy" "nova_policy" {
  role = aws_iam_role.nova_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"]
        Resource = "*"
      },
      {
        Effect = "Allow"
        Action = ["s3:GetObject", "s3:PutObject"]
        Resource = ["${aws_s3_bucket.input.arn}/*", "${aws_s3_bucket.output.arn}/*"]
      },
      {
        Effect = "Allow"
        Action = ["bedrock:InvokeModel", "comprehend:DetectPiiEntities"]
        Resource = "*" # Nova models are accessed via bedrock:InvokeModel
      }
    ]
  })
}

# Lambda Function
resource "aws_lambda_function" "nova_agent" {
  filename      = "lambda_function.zip"
  function_name = "NovaGuardAgent"
  role          = aws_iam_role.nova_role.arn
  handler       = "src/lambda_function.lambda_handler"
  runtime       = "python3.11"
  timeout       = 180 # Nova Lite 2 reasoning takes longer
}
