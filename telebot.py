import asyncio
import random
from datetime import datetime
from telegram import Bot

# TOKEN ของบอท
TOKEN = '7918608396:AAG_e0h8qDD7IglKUFanyvC9UwKo8kiDqmE'

# กลุ่มเป้าหมายยิงข้อความ
TARGET_CHAT_ID = '-1002533946981'  # หรือ @groupname

# ข้อความที่จะสุ่มยิง
messages = [
    "🔥 โปรโมชั่นใหม่ล่าสุด สมัครเลย!",
    "🎰 สล็อตแตกง่าย 2025 แจกกระจาย!",
    "🏆 คาสิโนสดระดับพรีเมียม!",
]

# เวลาที่ยิง (เฉพาะชั่วโมง)
post_hours = [10, 14, 20]  # 10.00 น., 14.00 น., 20.00 น.

async def auto_post():
    bot = Bot(token=TOKEN)
    last_shot = None  # ไว้เก็บว่า "วันนี้ยิงไปยัง" (กันยิงซ้ำชั่วโมงเดียวกัน)

    while True:
        now = datetime.now()

        # เช็กว่า ชั่วโมงนี้ตรงกับเวลาตั้งไหม
        if now.hour in post_hours:
            # และยังไม่เคยยิงในชั่วโมงนี้
            if last_shot != now.hour:
                message = random.choice(messages)
                try:
                    await bot.send_message(chat_id=TARGET_CHAT_ID, text=message, parse_mode='HTML')
                    print(f"✅ ยิงข้อความสำเร็จ ({now.strftime('%H:%M')}) : {message}")
                except Exception as e:
                    print(f"❌ ยิงข้อความล้มเหลว: {e}")

                last_shot = now.hour  # อัปเดตว่าชั่วโมงนี้ยิงแล้ว

        # รอ 1 นาทีแล้วเช็กใหม่
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(auto_post())
