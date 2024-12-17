```markdown
# Telegram Payment Proof Bot

This Python script is a Telegram bot that generates and sends random payment proofs to a Telegram channel at regular intervals.

## Getting Started

To use this bot, you'll need to create a Telegram bot and obtain its token. Here's how:

1. Open the Telegram app and search for the "BotFather" bot.
2. Start a chat with BotFather and use the `/newbot` command to create a new bot.
3. Follow the instructions to choose a name and username for your bot.
4. Once your bot is created, BotFather will provide you with a token. **Keep this token private and do not share it with anyone.**

### Prerequisites

- Python 3.x
- telebot library
  ```bash
  pip install pyTelegramBotAPI
  ```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dabiexe/telegram-payment-proof-bot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd telegram-payment-proof-bot
   ```

3. Replace `'YOUR_TOKEN'` in the script with your actual Telegram bot token.

4. Replace `'@channelusername'` in the script with the username of your Telegram channel where you want to send payment proofs.

5. Run the script:

   ```bash
   python bot.py
   ```

## Usage

- The bot generates random payment proofs and sends them to the specified Telegram channel at regular intervals.
- You can customize the interval by adjusting the `time.sleep()` function in the script.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) library for providing an easy-to-use interface for Telegram bots.
```
