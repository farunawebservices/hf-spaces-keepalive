# 🔥 HuggingFace Spaces Keepalive

Automated GitHub Actions workflow to keep HuggingFace Spaces alive by pinging them every 6 hours.

## 🎯 Purpose

HuggingFace Spaces on free tier sleep after 48 hours of inactivity. This workflow prevents that by automatically visiting each Space URL every 6 hours.

## 📋 Monitored Spaces

- 🛡️ [Red-Teaming LLMs](https://faruna01-red-teaming-llms.hf.space)
- 🌐 [Igala NMT Translator](https://faruna01-igala-nmt-translator.hf.space)
- 🔬 [Igala Interpretability](https://faruna01-igala-mbert-interpretability.hf.space)
- ⚡ [Igala GPT from Scratch](https://faruna01-igala-gpt-from-scratch.hf.space)
- 🌍 [Igala Dataset Explorer](https://faruna01-igala-streamlit-app-02.hf.space)

## ⏰ Schedule

- **Automatic**: Every 6 hours (00:00, 06:00, 12:00, 18:00 UTC)
- **Manual**: Can be triggered manually from GitHub Actions tab

## 🚀 How It Works

1. GitHub Actions runs on a schedule
2. Python script sends HTTP GET requests to each Space
3. Logs success/failure for each Space
4. Workflow fails if any Space is down (for monitoring)

## 📊 Monitoring

Check workflow runs at: [Actions Tab](https://github.com/farunawebservices/hf-spaces-keepalive/actions)

## 🛠️ Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run keepalive script
python keepalive.py

📄 License
MIT License