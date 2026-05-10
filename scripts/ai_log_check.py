from ollama import Client
import subprocess
import os

client = Client(host=os.getenv("OLLAMA_HOST", "http://localhost:11434"))

# لاگ‌های آخرین deploy رو از Docker بگیر
logs = subprocess.check_output(
    ["kubectl", "logs", "--tail", "100", 
     "deployment/my-app", "-n", "default"],
    stderr=subprocess.STDOUT
).decode()

response = client.chat(
    model="llama3.2:1b",
    messages=[{
        "role": "user",
        "content": f"""
Analyze these deployment logs. 
Find errors, warnings, or anomalies.
Give a short summary (3 lines max).

Logs:
{logs}
"""
    }]
)

print(response["message"]["content"])