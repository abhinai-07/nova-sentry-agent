# NovaSentry Agent: Autonomous Compliance & Secure AI-Ops

NovaSentry Agent Architecture <img width="4675" height="3698" alt="image" src="https://github.com/user-attachments/assets/b35f6ab4-825c-4c0c-a9f2-ed9a7c5ce8f8" />


**NovaSentry Agent** is a cloud-native, autonomous compliance agent built for the Amazon Nova AI Hackathon. It bridges the gap between high-speed AI processing and stringent data security by using agentic reasoning to categorize documents while enforcing a "Zero Trust" PII (Personally Identifiable Information) filtering layer.

---

## 🚀 Core Pillars

### 1. Security & Compliance (The Shield)
* **Zero-Exfiltration PII Filter:** A local regex-based pre-processing layer that intercepts and masks sensitive Indian identifiers like Aadhaar and PAN cards before they reach the LLM.
* **Least Privilege Access:** IAM roles are scoped strictly to the resources required for document processing.

### 2. AI & Agentic Reasoning (The Brain)
* **Amazon Nova 2 Lite:** Leverages high-performance LLMs to perform intelligent document categorization.
* **Priority Determination:** The agent doesn't just read; it decides the urgency of the data based on its content, simulating a real-world SRE/DevOps ticketing workflow.

### 3. Automation & Infrastructure (The Backbone)
* **Infrastructure as Code (IaC):** 100% of the AWS environment (S3, Lambda, Bedrock configurations) is defined and deployed via **Terraform**.
* **CI/CD Pipeline:** Integrated **GitHub Actions** to automate testing and deployment, ensuring every infrastructure change is tracked.

---

## 🛠️ Tech Stack
* **Cloud:** AWS (S3, Lambda, IAM, Amazon Bedrock)
* **AI Model:** Amazon Nova 2 Lite
* **DevOps:** Terraform, GitHub Actions
* **Language:** Python 3.x
* **Security:** Regex-based PII Masking

---

## 🏁 Getting Started

### Prerequisites
* AWS CLI configured with appropriate permissions.
* Terraform installed.
* Python 3.9+ for local testing.

### Deployment
1. **Clone the repo:**
   ```bash
   git clone https://github.com/abhinai-07/nova-sentry-agent.git
   cd nova-sentry-agent
2. **Initialize Terraform:
   ```bash
   cd src/
   terraform init
   terraform apply -auto-approve
### 🛡️ License
* Distributed under the MIT License. See LICENSE for more information.
