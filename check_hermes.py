import requests
import hashlib
import os

urls = [
    "https://www.hermes.com/jp/ja/product/%E3%83%90%E3%83%83%E3%82%B0-%E3%80%8A%E3%83%94%E3%82%B3%E3%82%BF%E3%83%B3%E3%83%BB%E3%83%AD%E3%83%83%E3%82%AF%E3%80%8B-18-H056289CC3Y/",
    "https://www.hermes.com/jp/ja/product/%E3%83%90%E3%83%83%E3%82%B0-%E3%80%8A%E3%83%94%E3%82%B3%E3%82%BF%E3%83%B3%E3%83%BB%E3%83%AD%E3%83%83%E3%82%AF%E3%80%8B-18-H056289CK8L/",
    "https://www.hermes.com/jp/ja/product/%E3%83%90%E3%83%83%E3%82%B0-%E3%80%8A%E3%83%94%E3%82%B3%E3%82%BF%E3%83%B3%E3%83%BB%E3%83%AD%E3%83%83%E3%82%AF%E3%80%8B-18-H056289CK18/",
    "https://www.hermes.com/jp/ja/product/%E3%83%90%E3%83%83%E3%82%B0-%E3%80%8A%E3%83%94%E3%82%B3%E3%82%BF%E3%83%B3%E3%83%BB%E3%83%AD%E3%83%83%E3%82%AF%E3%80%8B-18-H073597CKD0/",
    "https://www.hermes.com/jp/ja/product/%E3%83%90%E3%83%83%E3%82%B0-%E3%80%8A%E3%83%94%E3%82%B3%E3%82%BF%E3%83%B3%E3%83%BB%E3%83%AD%E3%83%83%E3%82%AF%E3%80%8B-18-H056289CC8L/",
    "https://www.hermes.com/jp/ja/product/%E3%83%90%E3%83%83%E3%82%B0-%E3%80%8A%E3%83%94%E3%82%B3%E3%82%BF%E3%83%B3%E3%83%BB%E3%83%AD%E3%83%83%E3%82%AF%E3%80%8B-18-H056289CC18/",
    "https://www.hermes.com/jp/ja/product/%E3%83%90%E3%83%83%E3%82%B0-%E3%80%8A%E3%83%94%E3%82%B3%E3%82%BF%E3%83%B3%E3%83%BB%E3%83%AD%E3%83%83%E3%82%AF%E3%80%8B-18-H073597CCD0/"
]

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK")

def fetch_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    return response.text

def get_hash(content):
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

def main():
    for url in urls:
        content = fetch_content(url)
        content_hash = get_hash(content)
        hash_file = f".hash_{get_hash(url)}"

        old_hash = None
        if os.path.exists(hash_file):
            with open(hash_file, "r") as f:
                old_hash = f.read()

        if old_hash != content_hash:
        　　 print(f"URL: {url}")
    　　　　 print(f"Old hash: {old_hash}")
    　　　　 print(f"New hash: {content_hash}")

　　　　　　　message = f"📢 ページが更新されました: {url}"
            requests.post(WEBHOOK_URL, json={"text": message})

            with open(hash_file, "w") as f:
                f.write(content_hash)

if __name__ == "__main__":
    main()
