variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "steps"
}

variable "environment" {
  description = "Environment (dev/staging/prod)"
  type        = string
  default     = "dev"
}

variable "external_sns_topic_arn" {
  description = "ARN of the external SNS topic that will trigger the Lambda function"
  type        = string
} 
