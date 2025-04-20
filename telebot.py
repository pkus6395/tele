import asyncio
import random
from telegram import Bot
from datetime import datetime

# Bot Token
TOKEN = '7918608396:AAG_e0h8qDD7IglKUFanyvC9UwKo8kiDqmE'

# Target Chat
TARGET_CHAT_ID = '-1002533946981'  # หรือ @groupname ก็ได้

# ข้อความที่จะยิงสุ่ม
messages = [
    "🔥 โปรใหม่มาแล้ว!",
    "🎰 สล็อตแตกง่ายทุกวัน!",
    "🏆 คาสิโนสด บริการระดับโลก!",
]

# ชั่วโมงที่ต้องยิงข้อความ
post_hours = [10, 14, 20]  # ยิงเวลา 10 โมง, 14 โมง, 20.00 น.

async def auto_post():
    bot = Bot(token=TOKEN)

    while True:
        now = datetime.now()
        if now.hour in post_hours:
            message = random.choice(messages)
            try:
                await bot.send_message(chat_id=TARGET_CHAT_ID, text=message, parse_mode='HTML')
                print(f"✅ ยิงข้อความสำเร็จ: {message}")
            except Exception as e:
                print(f"❌ ยิงข้อความล้มเหลว: {e}")
            await asyncio.sleep(3700)  # รอประมาณ 1 ชั่วโมง
        else:
            await asyncio.sleep(600)  # รอ 10 นาทีแล้วเช็กใหม่

if __name__ == "__main__":
    asyncio.run(auto_post())
