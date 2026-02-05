variable "aws_region" {
  description = "The AWS region to deploy in"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for resource naming"
  default     = "novasentry"
}

variable "lambda_timeout" {
  description = "Timeout for Nova reasoning (seconds)"
  default     = 180
}

variable "model_id" {
  description = "The Amazon Nova model inference profile ID"
  default     = "us.amazon.nova-2-lite-v1:0"
}
