NovaSentry Agent: ![NovaSentry Agent Architecture](./NovaSentry%20Agent.png)Autonomous Compliance & Secure AI-Ops
NovaSentry Agent is a cloud-native, autonomous compliance agent built for the Amazon Nova AI Hackathon. It bridges the gap between high-speed AI processing and stringent data security by using agentic reasoning to categorize documents while enforcing a "Zero Trust" PII (Personally Identifiable Information) filtering layer.

🚀 Core Pillars
1. Security & Compliance (The Shield)
Zero-Exfiltration PII Filter: A local regex-based pre-processing layer that intercepts and masks sensitive Indian identifiers (Aadhaar, PAN cards) before they ever reach the LLM.

Least Privilege Access: IAM roles are scoped strictly to the resources required for document processing.

2. AI & Agentic Reasoning (The Brain)
Amazon Nova 2 Lite: Leverages high-performance LLMs to perform intelligent document categorization.

Priority Determination: The agent doesn't just read; it decides the urgency of the data based on its content, simulating a real-world SRE/DevOps ticketing workflow.

3. Automation & Infrastructure (The Backbone)
Infrastructure as Code (IaC): 100% of the AWS environment (S3, Lambda, Bedrock configurations) is defined and deployed via Terraform.

CI/CD Pipeline: Integrated GitHub Actions to automate testing and deployment, ensuring that every infrastructure change is tracked and validated.

🛠️ Tech Stack
Cloud: AWS (S3, Lambda, IAM, Amazon Bedrock)

AI Model: Amazon Nova 2 Lite

DevOps: Terraform, GitHub Actions

Language: Python 3.x

Security: Regex-based PII Masking

📐 Architecture
Ingestion: Documents are uploaded to an S3 bucket.

Security Gate: A Lambda function triggers, running a PII scan. If sensitive data is found, it is redacted.

Intelligence: The "clean" text is sent to Amazon Nova. The model categorizes the file (e.g., Technical, Legal, Urgent).

Action: Results are stored in a processed S3 bucket with metadata tags for easy searching.

🏁 Getting Started
Prerequisites
AWS CLI configured with appropriate permissions.

Terraform installed.

Python 3.9+ for local testing.

Deployment
Clone the repo:

Bash

git clone https://github.com/abhinai-07/nova-sentry-agent.git
cd NovaSentry-Agent
Initialize Terraform:

Bash

cd terraform/
terraform init
terraform apply -auto-approve
📈 Future Roadmap
Integrate Amazon DynamoDB for real-time compliance logging.

Add Support for multi-lingual PII detection.

Dashboard visualization using Amazon QuickSight.

🛡️ License
Distributed under the MIT License. See LICENSE for more information.
