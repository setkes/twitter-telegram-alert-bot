# 🐦📲 Twitter → Telegram Alert Bot

A **Python bot** that monitors a specific Twitter account and sends **real-time notifications on Telegram** whenever a new tweet is posted.

---

## 🚀 Features

- ✅ Uses **Twitter API v2** (`search/recent`)
- 🔍 Monitors tweets from a specific user
- 📬 Sends instant alerts to **Telegram** (bot + chat ID)
- ♻️ Runs in a loop and checks every **15 seconds**

---

## 📦 Requirements

- Python **3.7+**
- **Twitter API v2 access** (at least **Basic tier**: `$200/month`)  
  → required to use the `search/recent` endpoint
- A Telegram bot via [@BotFather](https://t.me/BotFather)
- Your Telegram `chat_id` (user or group)

---

## ⚙️ Setup

### 🔁 1. Clone the repository

```bash
git clone https://github.com/yourusername/twitter-telegram-alert-bot.git
cd twitter-telegram-alert-bot
