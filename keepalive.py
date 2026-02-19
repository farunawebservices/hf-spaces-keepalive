import requests
import time
from datetime import datetime

# Your HuggingFace Spaces URLs
SPACES = [
    "https://faruna01-red-teaming-llms.hf.space",
    "https://faruna01-igala-nmt-translator.hf.space",
    "https://faruna01-igala-mbert-interpretability.hf.space",
    "https://faruna01-igala-gpt-from-scratch.hf.space",
    "https://faruna01-igala-streamlit-app-02.hf.space",
    "https://huggingface.co/spaces/Faruna01/lsr-dashboard",
]

def ping_space(url):
    """Ping a HuggingFace Space to keep it alive"""
    try:
        response = requests.get(url, timeout=30)
        status = "✅ ALIVE" if response.status_code == 200 else f"⚠️ Status {response.status_code}"
        print(f"{status} - {url}")
        return True
    except Exception as e:
        print(f"❌ FAILED - {url}: {str(e)}")
        return False

def main():
    print(f"\n🚀 HuggingFace Spaces Keepalive")
    print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"📍 Pinging {len(SPACES)} spaces...\n")
    
    results = []
    for space in SPACES:
        success = ping_space(space)
        results.append(success)
        time.sleep(2)  # Wait 2 seconds between requests
    
    success_count = sum(results)
    print(f"\n✅ Success: {success_count}/{len(SPACES)} spaces alive")
    
    if success_count < len(SPACES):
        print("⚠️ Warning: Some spaces are down!")
        exit(1)  # Exit with error code if any space failed

if __name__ == "__main__":
    main()
