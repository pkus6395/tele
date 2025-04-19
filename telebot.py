import asyncio
import random
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ใส่ Bot Token ที่ได้จาก @BotFather
TOKEN = '7918608396:AAE3lYhme_BCHaubuS9iBIgum2kWCRwAdNs'

# ตั้งค่าบอท
app = ApplicationBuilder().token(TOKEN).build()

# ตั้งชื่อกลุ่ม (แบบ public) ที่จะยิงข้อความ
group_usernames = [
    '-1002533946981'   # ใส่ชื่อกลุ่มที่ตั้ง Public ไว้
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
        await update.message.reply_text("🛠 ติดต่อแอดมินได้ที่ [คลิกที่นี่](https://play.ufa11k.co/signup?ref=aGWZqV)", parse_mode='Markdown')
    else:
        await update.message.reply_text("❓ กรุณาเลือกเมนูจากปุ่ม หรือพิมพ์ใหม่อีกครั้งครับ!")





# ฟังก์ชันรันพร้อมกัน
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
   
    app.run_polling()              # ฟังคำสั่ง /start
