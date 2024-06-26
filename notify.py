import asyncio
from telegram import Bot

async def send_telegram_message(token, chat_id, text):
    bot = Bot(token=token)
    try:
        await bot.send_message(chat_id=chat_id, text=text)
    except Exception as e:
        print(f"Error sending Telegram message: {e}")


if __name__ == "__main__":
    token = ""  # Replace this with your actual bot token
    chat_id = ""  # Replace this with the chat ID you obtained
    message = "This is a test message"
    asyncio.run(send_telegram_message(token, chat_id, message))
