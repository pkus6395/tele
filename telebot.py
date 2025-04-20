from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

TOKEN = '7918608396:AAG_e0h8qDD7IglKUFanyvC9UwKo8kiDqmE'
TARGET_CHAT_ID = '-1002533946981'

messages = [
    "🔥 โปรใหม่มาแรง!",
    "🎰 สล็อตแตกง่ายทุกวัน!",
    "🏆 คาสิโนสด ยิงตรงจากบ่อนจริง!",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🎯 สมัคร", "🎁 โปรโมชั่น"], ["🛠 ติดต่อแอดมิน"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "✅ ยินดีต้อนรับสู่ Casino168!\nเลือกเมนูที่ต้องการได้เลย 👇",
        reply_markup=reply_markup
    )

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "สมัคร" in text:
        await update.message.reply_text("✅ สมัครที่นี่ [คลิก](https://play.ufa11k.co/signup?ref=aGWZqV)", parse_mode='Markdown')
    elif "โปร" in text:
        await update.message.reply_text("🎁 โปรใหม่ที่ [คลิก](https://play.ufa11k.co/signup?ref=aGWZqV)", parse_mode='Markdown')
    elif "ติดต่อ" in text:
        await update.message.reply_text("🛠 ติดต่อแอดมินที่ @Casino168_Support", parse_mode='Markdown')
    else:
        await update.message.reply_text("❓ กรุณาเลือกเมนูจากปุ่ม หรือพิมพ์ใหม่อีกครั้งครับ!")

async def send_random_message(context: ContextTypes.DEFAULT_TYPE):
    message = random.choice(messages)
    try:
        await context.bot.send_message(chat_id=TARGET_CHAT_ID, text=message, parse_mode='HTML')
        print(f"✅ ยิงข้อความสำเร็จ: {message}")
    except Exception as e:
        print(f"❌ ยิงข้อความล้มเหลว: {e}")

if __name__ == '__main__':
    # ✅ ต้อง post_init=True ตรงนี้!
    app = ApplicationBuilder().token(TOKEN).post_init(True).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, reply_message))

    # ✅ จากนั้นยิงโพสต์ได้ถูกต้อง
    app.job_queue.run_repeating(send_random_message, interval=3600, first=10)

    app.run_polling()
