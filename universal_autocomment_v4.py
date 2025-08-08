
from telethon import TelegramClient, events
import asyncio

print("🔐 Вхідні дані для запуску Telegram-бота:")
try:

api_id = int(input("api_id: "))
api_hash = input("api_hash: ")
chat_input = input("Список чатів (через кому): ")
target_chats = [c.strip() for c in chat_input.split(',')]
comment_text = input("Текст коментаря: ")

client = TelegramClient('user_session', api_id, api_hash)

async def comment_on_last_message():
    for chat in target_chats:
        try:
            messages = await client.get_messages(chat, limit=1)
            if messages:
                message = messages[0]
                # Щоб не дублювати, перевір чи ти вже коментував:
                replies = await message.get_replies()
                me = await client.get_me()
                already_commented = any(reply.sender_id == me.id for reply in replies)
                if not already_commented:
                    await message.reply(comment_text)
                    print(f"✅ Прокоментовано: {chat}")
                else:
                    print(f"⏭ Уже коментував у: {chat}")
        except Exception as e:
            print(f"⚠️ Помилка в {chat}: {e}")

with client:
    client.loop.run_until_complete(comment_on_last_message())
    

    print("\n🚀 Бот запущено. Очікуємо нові повідомлення...")
    client.start()
    client.run_until_disconnected()

except Exception as e:
    print(f"❌ Сталася помилка: {e}")
    input("Натисніть Enter для виходу...")
