import boto3
import json
import re

# Initialize clients - Note: Bedrock is in us-east-1 for Nova availability
s3 = boto3.client('s3')
bedrock = boto3.client('bedrock-runtime', region_name="us-east-1")

def lambda_handler(event, context):
    # 1. Capture S3 Event Details
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        # 2. Get document from S3
        print(f"Fetching file: {key} from bucket: {bucket}")
        obj = s3.get_object(Bucket=bucket, Key=key)
        text = obj['Body'].read().decode('utf-8')

        # 3. LOCAL SECURITY GATE (Replaces Amazon Comprehend)
        # Regex for Aadhaar (India), PAN Card, and Email
        aadhaar_pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
        pan_pattern = r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b'
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

        if re.findall(aadhaar_pattern, text) or re.findall(pan_pattern, text) or re.findall(email_pattern, text):
            print(f"SECURITY ALERT: PII detected in {key}. Blocking execution.")
            return {
                "status": "BLOCKED",
                "reason": "Sensitive PII (Aadhaar/PAN/Email) detected by Local Security Gate."
            }

        # 4. AGENTIC REASONING (Amazon Nova 2 Lite)
        print("PII scan passed. Invoking Amazon Nova 2 Lite...")
        model_id = "us.amazon.nova-2-lite-v1:0"

        system_prompt = (
            "You are the NovaGuard Agent. Analyze the text and return a JSON object with: "
            "1. 'doc_type' (Invoice, Contract, or Note), "
            "2. 'priority' (High/Low), "
            "3. 'action_taken' (A 2-sentence summary)."
            "Return ONLY raw JSON."
        )

        messages = [{"role": "user", "content": [{"text": text}]}]

        response = bedrock.converse(
            modelId=model_id,
            messages=messages,
            system=[{"text": system_prompt}],
            inferenceConfig={"maxTokens": 600, "temperature": 0.1}
        )

        # Extract reasoning result
        result = response['output']['message']['content'][0]['text']

        # 5. Save reasoning output to the results bucket
        output_bucket = bucket.replace("-input-", "-output-") # Adjusted for standard naming
        s3.put_object(
            Bucket=output_bucket,
            Key=f"analysis-{key}.json",
            Body=result,
            ContentType='application/json'
        )

        print(f"Successfully processed {key}. Result saved to {output_bucket}.")
        return {"status": "SUCCESS"}

    except Exception as e:
        print(f"Error encountered: {str(e)}")
        return {"status": "FAILED", "error": str(e)}
