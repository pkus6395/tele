
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# TOKEN Bot
TOKEN = '7918608396:AAE3lYhme_BCHaubuS9iBIgum2kWCRwAdNs'

# กลุ่มหรือแชทที่จะยิง
TARGET_CHAT_ID = '-1002533946981'  # หรือใช้ @groupname ก็ได้

# ข้อความที่สุ่มยิง
messages = [
    "🔥 โปรโมชั่นมาใหม่ แจกหนัก!",
    "🎯 สล็อตแตกง่าย 2025 กำลังมาแรง!",
    "🏆 คาสิโนสด บริการระดับพรีเมียม!",
]

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
async def send_random_message(context: ContextTypes.DEFAULT_TYPE):
    message = random.choice(messages)
    try:
        await context.bot.send_message(chat_id=TARGET_CHAT_ID, text=message, parse_mode='HTML')
        print(f"✅ ยิงข้อความสำเร็จ: {message}")
    except Exception as e:
        print(f"❌ ยิงข้อความล้มเหลว: {e}")

# เริ่มทำงาน
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, reply_message))

    job_queue = app.job_queue
    job_queue.run_repeating(send_random_message, interval=3600, first=10)

    app.run_polling()
