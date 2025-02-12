# Color picker Bot

A Telegram bot built with `python-telegram-bot` 13.15 that helps users pick a color using an RGB palette. The bot is connected to a web app, allowing users to select a color interactively and receive its RGB and HEX values.

## Features
- 🌈 Interactive color picker
- 🎨 Displays RGB and HEX values after selection
- 🌐 WebApp integration for seamless color selection
  
## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/HusniyorAzimboyev/color-picker-bot.git
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
1. Obtain a Telegram bot token from [BotFather](https://t.me/BotFather).
2. Set up your environment variables in main.py:
   ```sh
   TOKEN=your_bot_token_here
   ADMIN=your_telegram_id_here
   ```

## Usage
Run the bot with:
```sh
python main.py
```
Once running, start a chat with your bot and interact with the color picker WebApp.

## Technologies Used
- `python-telegram-bot`
- WebApp for color selection
- RGB to HEX conversion
