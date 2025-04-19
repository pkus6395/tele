import asyncio
import random
from datetime import datetime
from telegram import Bot

# ใส่ Token บอท
TOKEN = '7918608396:AAE3lYhme_BCHaubuS9iBIgum2kWCRwAdNs'

# ตั้งชื่อกลุ่ม public หรือ Group ID
TARGET_CHAT = '-1002533946981'  # หรือ '-100xxxxxxxxxx' ถ้าใช้ Group ID

# ข้อความที่จะยิงสุ่ม
messages = [
    "🔥 โปรโมชั่นมาใหม่ แจกหนัก!",
    "🎯 สล็อตแตกง่าย 2025 กำลังมาแรง!",
    "🏆 คาสิโนสด บริการระดับพรีเมียม!",
]

# ชั่วโมงที่จะยิงข้อความ (24 ชม.)
post_hours = [10, 14, 20]

# ฟังก์ชันยิงข้อความอัตโนมัติ
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
                print(f"❌ ยิงข้อความล้มเหลว: {e}")

            await asyncio.sleep(3700)  # รอประมาณ 1 ชม.ก่อนยิงใหม่
        else:
            await asyncio.sleep(600)  # เช็กทุก ๆ 10 นาที

# รัน
if __name__ == '__main__':
    asyncio.run(auto_post())
