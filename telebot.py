import asyncio
import random
from telegram import Bot
from datetime import datetime

# TOKEN Bot
TOKEN = '7918608396:AAG_e0h8qDD7IglKUFanyvC9UwKo8kiDqmE'

# ID ของกลุ่ม หรือ @username
TARGET_CHAT_ID = '-1002533946981'

# ข้อความที่สุ่มยิง
messages = [
    "🔥 โปรโมชั่นมาใหม่!",
    "🎰 สล็อตแตกง่ายทุกวัน!",
    "🏆 คาสิโนสดระดับโลก!",
]

# เวลาที่ยิงโพสต์ (ชั่วโมง)
post_hours = [10, 14, 20]  # 10 โมง, 14 โมง, 2 ทุ่ม

async def send_post():
    bot = Bot(token=TOKEN)

    while True:
        now = datetime.now()
        if now.hour in post_hours:
            message = random.choice(messages)
            try:
                await bot.send_message(chat_id=TARGET_CHAT_ID, text=message, parse_mode='HTML')
                print(f"✅ ยิงข้อความสำเร็จ: {message}")
            except Exception as e:
                print(f"❌ ยิงล้มเหลว: {e}")

            await asyncio.sleep(3700)  # รอประมาณ 1 ชม. ก่อนยิงใหม่
        else:
            await asyncio.sleep(600)  # รอ 10 นาทีเช็กอีกที

if __name__ == "__main__":
    asyncio.run(send_post())
