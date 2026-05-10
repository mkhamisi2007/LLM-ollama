from ollama import Client
import sys
import os

client = Client(host=os.getenv("OLLAMA_HOST", "http://localhost:11434"))

def review_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    response = client.chat(
        model="llama3.2:1b",
        messages=[{
            "role": "user",
            "content": f"""
You are a DevOps engineer. Review this file for:
1. Security issues
2. Best practice violations
3. Misconfigurations

File: {filepath}
---
{content}
---^
IMPORTANT: Your FIRST word must be FAIL or PASS (nothing before it).
Then list issues as bullet points.
If any security issue exists, you MUST reply FAIL.
"""
        }]
    )

    result = response["message"]["content"]
    print(f"\n=== Review: {filepath} ===\n{result}")

    # keyword-based detection - مستقل از مدل
    danger_keywords = [
        "secret_key", "db_password", "hardcode", "hard-coded",
        "privileged: true", "privileged:true",
        "0.0.0.0/0", "public-read", "access_key", "secret_key",
        "latest", "root user", "no resource limit",
        "no liveness", "no readiness"
    ]

    content_lower = content.lower()
    result_lower = result.lower()

    has_danger_in_file = any(k in content_lower for k in danger_keywords)
    has_fail_in_review = "fail" in result_lower

    if has_danger_in_file or has_fail_in_review:
        print(f">>> PIPELINE FAILED for: {filepath}")
        sys.exit(1)
    else:
        print(f">>> PASSED: {filepath}")

# فایل‌هایی که باید چک بشن
files_to_review = [
    "Dockerfile",
    "k8s/deployment.yaml",
    "terraform/main.tf"
]

for f in files_to_review:
    if os.path.exists(f):
        review_file(f)
