import random
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Bot Token
TOKEN = '7918608396:AAHunKDouPqGXYC4EGHrUqG09vKjw4IoqwQ'

# กลุ่มยิงข้อความ
group_usernames = [
    '-1002533946981'
]

# ข้อความที่จะสุ่มยิง
messages = [
    "🔥 โปรโมชั่นใหม่! สมัครรับโบนัสทันที!",
    "🎯 คาสิโนสด ฝากถอนไว ไม่ง้อเอเย่นต์!",
    "🎰 สล็อตแตกง่าย 2025 เล่นได้ทุกวัน!",
]

# ชั่วโมงที่ต้องยิงข้อความ
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
        await update.message.reply_text('✅ สมัครสมาชิกได้ที่ <a href="https://play.ufa11k.co/signup?ref=aGWZqV">คลิกที่นี่</a>', parse_mode='HTML')
    elif "โปร" in text:
        await update.message.reply_text('🎁 ดูโปรโมชันล่าสุดได้ที่ <a href="https://play.ufa11k.co/signup?ref=aGWZqV">โปรโมชันคาสิโน</a>', parse_mode='HTML')
    elif "ติดต่อ" in text:
        await update.message.reply_text("🛠 ขออภัยค่ะ มันจบแล้ว เว็บเราบิดอย่างเดียวนะคะt")   
    else:
        await update.message.reply_text("❓ กรุณาเลือกเมนูจากปุ่ม หรือพิมพ์ใหม่อีกครั้งครับ!")

# ฟังก์ชันยิงข้อความสุ่ม
async def send_random_message(context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    current_hour = now.hour
    if current_hour in post_hours:
        selected_message = random.choice(messages)
        selected_group = random.choice(group_usernames)
        try:
            await context.bot.send_message(chat_id=selected_group, text=selected_message, parse_mode='HTML')
            print(f"✅ ยิงข้อความ: {selected_message} ไปที่ {selected_group} ({now.strftime('%H:%M')})")
        except Exception as e:
            print(f"❌ ยิงไม่สำเร็จ: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, reply_message))

    # ยิงข้อความทุก 1 นาที และเช็กว่าตรงเวลาที่ต้องยิงไหม
    app.job_queue.run_repeating(send_random_message, interval=60, first=10)

    app.run_polling()
