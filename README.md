# Twitter Telegram Alert Bot

This Python script monitors a specific Twitter account and sends real-time Telegram notifications when new tweets are posted.

## Features

- Uses Twitter API v2 (`search/recent` endpoint)
- Monitors tweets from a specific user
- Sends alerts to your Telegram via bot
- Runs in a loop and checks every 15 seconds

## Requirements

- Python 3.7+
- Twitter API **Basic access level (at least $200/month)** – required to use the `search/recent` endpoint.
- A Telegram bot already created via [@BotFather](https://t.me/BotFather)
- Your Telegram user or group chat ID

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/twitter-telegram-alert-bot.git
cd twitter-telegram-alert-bot
