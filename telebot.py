import asyncio
import random
from datetime import datetime
from telegram import Bot

TOKEN = '7918608396:AAE3lYhme_BCHaubuS9iBIgum2kWCRwAdNs'
TARGET_CHAT = '-1002533946981'  # หรือ '-100xxxxxxxxxx'

messages = [
    "🔥 โปรโมชั่นมาใหม่ แจกหนัก!",
    "🎯 สล็อตแตกง่าย 2025 กำลังมาแรง!",
    "🏆 คาสิโนสด บริการระดับพรีเมียม!",
]

post_hours = [10, 14, 20]

async def auto_post():
    bot = Bot(token=TOKEN)

    while True:
        current_hour = datetime.now().hour
        if current_hour in post_hours:
            selected_message = random.choice(messages)
            try:
                await bot.send_message(chat_id=TARGET_CHAT, text=selected_message, parse_mode='HTML')
                print(f"✅ ยิงข้อความสำเร็จ: {selected_message} ไปที่ {TARGET_CHAT}")
            except Exception as e:
                print(f"❌ ยิงไม่สำเร็จ: {e}")

            await asyncio.sleep(3700)  # รอประมาณ 1 ชม.
        else:
            await asyncio.sleep(600)  # เช็กทุก ๆ 10 นาที

if __name__ == '__main__':
    asyncio.run(auto_post())
