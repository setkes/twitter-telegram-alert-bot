# Twitter Telegram Alert Bot - Installation Guide

This guide explains how to set up and run the **Twitter Telegram Alert Bot** step by step.

## Prerequisites

Before starting, make sure you have:

- A Twitter Basic API subscription (Twitter Developer Account)
- A Telegram Bot (created through BotFather)

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/twitter-telegram-alert-bot.git
cd twitter-telegram-alert-bot
```

## 2. Set up the environment

### On Linux/macOS:

```bash
# Create virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### On Windows:

```bash
# Create virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

## 3. Create the .env configuration file

In the root of the project, create a file named `.env` and add the following variables:

```
BEARER_TOKEN=your_twitter_bearer_token
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
TWITTER_USERNAME=Fifacom
```

## 4. Run the bot

Once everything is configured, run:

```bash
python main.py
```
