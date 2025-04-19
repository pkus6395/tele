import asyncio
import random
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ใส่ Token บอท
TOKEN = '7918608396:AAE3lYhme_BCHaubuS9iBIgum2kWCRwAdNs'

# ตั้งค่าบอท
app = ApplicationBuilder().token(TOKEN).build()

# ตั้งชื่อกลุ่ม
group_usernames = [
    '-1002533946981'
]

# ข้อความสุ่ม
messages = [
    "🔥 โปรโมชั่นมาใหม่ แจกหนัก!",
    "🎯 สล็อตแตกง่าย 2025 กำลังมาแรง!",
    "🏆 คาสิโนสด บริการระดับพรีเมียม!",
]

# ชั่วโมงที่จะยิงข้อความ
post_hours = [10, 14, 20]

# ฟังก์ชันตอบ /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🎯 สมัคร", "🎁 โปรโมชั่น"], ["🛠 ติดต่อแอดมิน"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "✅ ยินดีต้อนรับสู่ Casino168!\nเลือกเมนูที่คุณต้องการได้เลย 👇",
        reply_markup=reply_markup
    )

# ฟังก์ชันตอบข้อความทั่วไป
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "สมัคร" in text:
        await update.message.reply_text("✅ สมัครสมาชิกได้ที่ [คลิกที่นี่](https://play.ufa11k.co/signup?ref=aGWZqV)", parse_mode='Markdown')
    elif "โปร" in text:
        await update.message.reply_text("🎁 ดูโปรโมชันล่าสุดได้ที่ [โปรโมชันคาสิโน](https://play.ufa11k.co/signup?ref=aGWZqV)", parse_mode='Markdown')
    elif "ติดต่อ" in text:
        await update.message.reply_text("🛠 ติดต่อแอดมินได้ที่ @Casino168_Support", parse_mode='Markdown')
    else:
        await update.message.reply_text("❓ กรุณาเลือกเมนูจากปุ่ม หรือพิมพ์ใหม่อีกครั้งครับ!")

# ฟังก์ชันยิงข้อความสุ่ม
async def auto_post():
    await asyncio.sleep(5)  # รอให้ทุกอย่างเริ่มทำงานก่อน
    while True:
        current_hour = datetime.now().hour
        if current_hour in post_hours:
            selected_message = random.choice(messages)
            selected_group = random.choice(group_usernames)

            try:
                await app.bot.send_message(chat_id=selected_group, text=selected_message, parse_mode='HTML')
                print(f"✅ ยิงข้อความ: {selected_message} ไปที่ {selected_group}")
            except Exception as e:
                print(f"❌ ยิงไม่สำเร็จ: {e}")

            await asyncio.sleep(3700)
        else:
            await asyncio.sleep(600)

# ฟังก์ชันหลัก
async def main():
    # ผูก Handler
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, reply_message))

    # เริ่ม Task ยิงข้อความอัตโนมัติ
    asyncio.create_task(auto_post())

    # รันบอท (Polling)
    await app.run_polling()

# เริ่มรัน
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())  # ไม่ใช้ asyncio.run()
    loop.run_forever()         # ให้ Loop วิ่งตลอด
