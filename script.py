import asyncio
from telegram import Bot

async def get_chat_id(token):
    bot = Bot(token=token)
    updates = await bot.get_updates()
    for update in updates:
        print(update.message.chat.id)

if __name__ == "__main__":
    token = ""  # Replace this with your actual bot token
    asyncio.run(get_chat_id(token))


