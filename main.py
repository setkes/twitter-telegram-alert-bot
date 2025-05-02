import requests
import time
import os
from dotenv import load_dotenv

# === LOAD CONFIGURATION FROM .env ===
load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")

API_URL_RECENT = f"https://api.twitter.com/2/tweets/search/recent?query=from:{TWITTER_USERNAME}&max_results=10"

HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json",
}

# === MEMORY FOR ALREADY NOTIFIED TWEETS ===
last_tweet_id = None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)

def get_latest_tweets():
    response = requests.get(API_URL_RECENT, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"❌ Twitter API error: {response.status_code} - {response.text}")
        return []

if __name__ == "__main__":
    print("🔍 Starting tweet monitoring...")

    while True:
        try:
            latest_tweets = get_latest_tweets()

            if latest_tweets:
                last_tweet = latest_tweets[0]
                tweet_id = last_tweet["id"]
                tweet_text = last_tweet["text"]
                tweet_url = f"https://twitter.com/{TWITTER_USERNAME}/status/{tweet_id}"

                print("\n📜 Recent tweets:")
                for tweet in latest_tweets:
                    print(f"- {tweet['text']}")

                if tweet_id != last_tweet_id:
                    last_tweet_id = tweet_id
                    message = f"🚨 New tweet from {TWITTER_USERNAME}:\n{tweet_text}\n\n🔗 {tweet_url}"
                    print("\n" + message)
                    send_telegram_message(message)
                else:
                    print("\n✅ No new tweet.")

            else:
                print("\n❌ No tweets found.")

            print("⏳ Waiting for new tweets...")
            time.sleep(15)

        except KeyboardInterrupt:
            print("\n👋 Monitoring stopped by user.")
            break

        except Exception as e:
            print(f"❌ Error in main loop: {e}")
            time.sleep(30)
