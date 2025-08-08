
from telethon import TelegramClient, events
import asyncio

print("🔐 Вхідні дані для запуску Telegram-бота:")
try:
    api_id = int(input("Введіть свій api_id: "))
    api_hash = input("Введіть свій api_hash: ")
    chat_input = input("Введіть список чатів через кому (наприклад: t.me/group1,t.me/channel2): ")
    target_chats = [chat.strip() for chat in chat_input.split(',')]
    comment_text = input("Введіть текст коментаря, який має залишати бот: ")

    client = TelegramClient('user_session', api_id, api_hash)

    @client.on(events.NewMessage(chats=target_chats))
    async def handler(event):
        me = await client.get_me()
        if event.sender_id != me.id:
            await asyncio.sleep(2)
            await event.reply(comment_text)

    print("\n🚀 Бот запущено. Очікуємо нові повідомлення...")
    client.start()
    client.run_until_disconnected()

except Exception as e:
    print(f"❌ Сталася помилка: {e}")
    input("Натисніть Enter для виходу...")
