import asyncio
import random
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# BOT Token
bot_token = '7918608396:AAE3lYhme_BCHaubuS9iBIgum2kWCRwAdNs'

# ตั้งค่าบอท
app = ApplicationBuilder().token(bot_token).build()

# Group ID ที่จะยิงข้อความเข้า
group_ids = [
    '-100850576402'  # ตัวอย่าง Group ID
]

# ข้อความที่ใช้สุ่มยิง
messages = [
    "🔥 สมัครสมาชิกใหม่ รับโบนัส 100% วันนี้เท่านั้น!",
    "🎰 หมุนสล็อตฟรี ลุ้นเงินหมื่นทุกวัน!",
    "⚡ แทงบอลราคาน้ำดีที่สุด ฝากถอนออโต้!",
    "🎯 คาสิโนสด เล่นง่าย ได้เงินจริง พร้อมสูตรแจกฟรี!",
]

# ชั่วโมงที่ต้องการให้ยิงข้อความ
post_hours = [10, 14, 20]

# ===============================
# ฟังก์ชันตอบ /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🔥 สมัครสมาชิก", "🎁 ดูโปรโมชันล่าสุด"], ["🛠 ติดต่อทีมงาน"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "🎲 ยินดีต้อนรับสู่ Casino168!\nเลือกเมนูที่คุณต้องการได้เลย 👇",
        reply_markup=reply_markup
    )

# ฟังก์ชันตอบข้อความทั่วไป
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "สมัคร" in text:
        await update.message.reply_text("✅ สมัครง่าย ๆ คลิกเลย [สมัครสมาชิก](https://casino168.link/signup)", parse_mode='Markdown')
    elif "โปร" in text:
        await update.message.reply_text(
            "🎉 โปรโมชันใหม่!\n🔥 โบนัสสมาชิกใหม่ 100%\n💰 คืนยอดเสีย 5% ทุกสัปดาห์\n[ดูเพิ่มเติม](https://casino168.link/promotion)",
            parse_mode='Markdown'
        )
    elif "ติดต่อ" in text or "แอดมิน" in text:
        await update.message.reply_text(
            "🛠 ทีมงานพร้อมดูแล 24 ชั่วโมง!\n📩 ทักหาแอดมินที่ [@Casino168_Support](https://t.me/Casino168_Support)",
            parse_mode='Markdown'
        )
    else:
        await update.message.reply_text("❓ กรุณาเลือกเมนูจากปุ่ม หรือพิมพ์ใหม่อีกครั้งนะครับ!")

# ===============================
# ฟังก์ชันยิงข้อความสุ่มไปกลุ่ม
async def auto_post():
    while True:
        current_hour = datetime.now().hour
        if current_hour in post_hours:
            selected_message = random.choice(messages)
            selected_group = random.choice(group_ids)

            try:
                await app.bot.send_message(chat_id=selected_group, text=selected_message, parse_mode='HTML')
                print(f"✅ ส่งข้อความสำเร็จ: {selected_message} -> {selected_group}")
            except Exception as e:
                print(f"❌ ส่งไม่สำเร็จ: {e}")

            await asyncio.sleep(3700)  # รอประมาณ 1 ชม.
        else:
            print("⌛ รอถึงรอบโพสต์ถัดไป...")
            await asyncio.sleep(600)  # เช็กทุกๆ 10 นาที

# ===============================
# ผูก Handler
app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.TEXT, reply_message))

# ===============================
# ฟังก์ชันหลัก
async def run_bot():
    # Start Polling
    polling_task = asyncio.create_task(app.run_polling())
    # Start Auto Posting
    auto_post_task = asyncio.create_task(auto_post())
    # รันพร้อมกัน
    await asyncio.gather(polling_task, auto_post_task)

# ===============================
# เริ่มทำงาน
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot())
