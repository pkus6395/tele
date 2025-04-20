from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# TOKEN Bot
TOKEN = '7918608396:AAG_e0h8qDD7IglKUFanyvC9UwKo8kiDqmE'

# กลุ่มยิงข้อความ
TARGET_CHAT_ID = '-1002533946981'

# ข้อความสุ่ม
messages = [
    "🔥 โปรโมชั่นใหม่! สมัครรับโบนัสทันที!",
    "🎯 คาสิโนสด ฝากถอนไว ไม่ง้อเอเย่นต์!",
    "🎰 สล็อตแตกง่าย 2025 เล่นได้ทุกวัน!",
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
        print(f"✅ ยิงข้อความ: {message}")
    except Exception as e:
        print(f"❌ ยิงข้อความล้มเหลว: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, reply_message))

    # ใช้ JobQueue ยิงข้อความ
    app.job_queue.run_repeating(send_random_message, interval=3600, first=10)  # ยิงทุก 1 ชั่วโมง

    app.run_polling()  # ✅ เริ่มทำงาน ไม่ต้องสร้าง loop เอง, ไม่ error
