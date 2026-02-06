🛡️ NovaSentry Agent: The Sovereign AI Compliance Firewall
NovaSentry Agent is an autonomous, event-driven governance system built for the Amazon Nova AI Hackathon. It serves as a "Reasoning Firewall," leveraging Amazon Nova 2 Lite to interpret enterprise data while a local regex security gate identifies and blocks PII (Aadhaar, PAN, Email) before processing.

🚀 Key Features
Agentic Reasoning: Leverages Amazon Nova 2 Lite to autonomously categorize document intent and determine priority.

Sovereign Security Gate: Uses a high-performance local regex firewall to block sensitive PII (Aadhaar, PAN, Emails) with zero latency, ensuring data never leaves the environment for scanning.

Serverless Efficiency: Constructed on a fully event-driven architecture with AWS Lambda and Amazon S3.

Enterprise-Grade IaC: Managed through automated deployment and resource lifecycle control via Terraform.

🏗️ Architecture
Orchestration: AWS Lambda (Python 3.11).

AI Engine: Amazon Bedrock (Inference Profile: us.amazon.nova-2-lite-v1:0).

Storage: Amazon S3 (Isolated Input and Output Buckets).

Infrastructure: Terraform for repeatable, multi-environment deployments.

🛠️ Installation & Deployment
Prerequisites
AWS CLI configured for the us-east-1 region.

Terraform installed on your local machine.

Amazon Nova 2 Lite enabled within the Amazon Bedrock Console.

Steps
Bash

# 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/NovaSentry-Agent.git
cd NovaSentry-Agent

# 2. Initialize Terraform

terraform init

# 3. Deploy Infrastructure

terraform apply -auto-approve
🧹 Cleanup & Cost Management
To avoid ongoing AWS charges after the hackathon evaluation, use the following commands to remove the infrastructure.

Bash

# 1. Empty S3 Buckets (required before deletion)

aws s3 rm s3://YOUR_INPUT_BUCKET_NAME --recursive
aws s3 rm s3://YOUR_OUTPUT_BUCKET_NAME --recursive

# 2. Destroy Infrastructure

terraform destroy -auto-approve
📈 Challenges & Learnings
Cross-Region Inference: Successfully implemented Inference Profiles (us.) to manage on-demand throughput for the Nova model family.

Recursive Prevention: Engineered a one-way S3 pipeline to prevent infinite Lambda invocation loops.

Local Security Pivoting: Shifted from cloud-based PII detection to local regex to ensure lower latency and higher data privacy.
