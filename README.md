# LLM-with-Agentic-RAG-App

# Insight Reporter 🧠📊

**Insight Reporter** is a reporting tool that that leverages the power of AI tools such as TAVILY to provide insightful summary and readable links for further inquiry on  any queries this app makes it easy to gain insights quickly.

---

## 🚀 Features

- Generate Articles on Topical issues 
- Supports AI Agents tools
- Lightweight and Docker-ready

---

## 🐳 Run with Docker

### ✅ Pull from Docker Hub

```bash
docker pull damton/insight-reporter:latest


▶️ Run the container

docker run -p 8501:8501 damton/insight-reporter


Then open your browser at:

http://localhost:8501


🛠️ Build from source
Clone this repository and build the image manually:

git clone https://github.com/Dammyjosh/insight-reporter.git
cd insight-reporter
docker build -t insight-reporter .
docker run -p 8501:8501 insight-reporter

📦 Requirements (for local development)
If you're not using Docker:

pip install -r requirements.txt
streamlit run app.py


