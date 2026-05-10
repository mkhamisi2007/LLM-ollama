# 🤖 AI-Powered DevOps Pipeline

Integrating a Local LLM (Ollama) into a GitLab CI/CD pipeline for automated security review and log analysis.

---

## 📌 What This Project Does

Instead of using AI only to write code, this project embeds an LLM **directly inside the CI/CD pipeline** to:

- 🔍 **Review code automatically** before each merge request
- 📊 **Analyze deployment logs** after each deploy

---

## 🏗️ Project Structure

```
.
├── .gitlab-ci.yml          # Pipeline definition
├── scripts/
│   ├── ai_review.py        # AI-powered code review
│   └── ai_log_check.py     # AI-powered log analysis
├── Dockerfile              # Sample file with issues (for testing)
├── k8s/
│   └── deployment.yaml     # Kubernetes manifest (for testing)
└── terraform/
    └── main.tf             # Terraform config (for testing)
```

---

## ⚙️ Pipeline Stages

```
test → ai_review → build → deploy → ai_monitor
```

| Stage | Job | Description |
|-------|-----|-------------|
| `ai_review` | `ai_code_review` | LLM reviews Dockerfile, K8s manifests, Terraform |
| `ai_monitor` | `ai_log_analysis` | LLM reads deployment logs and detects anomalies |

---

## 🔍 How AI Review Works

`ai_review.py` sends each file to the LLM with this prompt:

```
You are a DevOps engineer. Review this file for:
1. Security issues
2. Best practice violations
3. Misconfigurations

IMPORTANT: Your FIRST word must be FAIL or PASS (nothing before it).
Then list issues as bullet points.
If any security issue exists, you MUST reply FAIL.
```

If the file contains known security issues (hardcoded secrets, privileged containers, open CIDR blocks...), the pipeline **fails automatically**.

---

## 🛠️ Stack

- **GitLab CI/CD** — pipeline orchestration
- **Python 3.11** — scripting
- **Ollama** — local LLM runtime (no API key needed)
- **llama3.2:1b** — lightweight model for fast inference
- **Kubernetes / Terraform / Docker** — reviewed infrastructure files

---

## 🚀 Run Locally

### 1. Install Ollama

```bash
# Linux/macOS
curl -fsSL https://ollama.com/install.sh | sh

# Pull the model
ollama pull llama3.2:1b
```

### 2. Clone and run

```bash
git clone https://github.com/YOUR_USERNAME/ai-devops-pipeline
cd ai-devops-pipeline

pip install ollama

python scripts/ai_review.py
```

### 3. Expected output

```
=== Review: Dockerfile ===
FAIL
- Hardcoded SECRET_KEY detected
- Using ubuntu:latest (no pinned version)
- No USER directive (runs as root)

>>> PIPELINE FAILED for: Dockerfile
```

---

## 💡 Key Concept

> The goal is not to replace the engineer,  
> but to give them an assistant that **never sleeps**. 🚀

---

## 📄 License

MIT
