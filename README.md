# Telegram Bot Project

This project is a Telegram bot that uses the OpenAI API to generate images based on user prompts and sends them back to the user within Telegram.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10.13 (runtime.txt)
- A Telegram bot token (obtained by registering a new bot with [@BotFather](https://t.me/botfather))
- An OpenAI API key (obtained by creating an account at [OpenAI](https://openai.com/))

## Installation

To install the Telegram bot, follow these steps:

1. Clone the repository:


2. Navigate to the project directory:


3. Create a virtual environment:

python -m venv venv


4. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On Unix or MacOS:

  ```
  source venv/bin/activate
  ```

5. Install the required packages:

pip install -r requirements.txt


## Setting Up Environment Variables

To keep your bot token and OpenAI API key secure, it's recommended to use environment variables. Create a `.env` file in the root directory of your project and add your bot token and OpenAI API key like so:


Replace `your_telegram_bot_token` and `your_openai_api_key` with the actual values.

> **Note**: If deploying to Heroku, set the environment variables in the Heroku dashboard instead of using a `.env` file.

## Running the Bot

To run the bot, execute the pthon file or push to Heroku


Your bot should now be up and running. Send `/faregpt` command to your bot in Telegram to start generating images.
