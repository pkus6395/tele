import telegram
import random
import time
from datetime import datetime

# BOT Token
bot_token = '7918608396:AAE3lYhme_BCHaubuS9iBIgum2kWCRwAdNs'
bot = telegram.Bot(token=bot_token)

# List ของข้อความที่จะสุ่มส่ง
messages = [
    "🔥 สมัครสมาชิกใหม่ รับโบนัส 100% วันนี้เท่านั้น!",
    "🎰 หมุนสล็อตฟรี ลุ้นเงินหมื่นทุกวัน!",
    "⚡ แทงบอลราคาน้ำดีที่สุด ฝากถอนออโต้!",
    "🎯 คาสิโนสด เล่นง่าย ได้เงินจริง พร้อมสูตรแจกฟรี!",
]

# List ของ Group ID ที่จะสุ่มส่ง
group_ids = [
    '-1007950882030'   # ตัวอย่างกลุ่ม 1
   
]

# กำหนดช่วงเวลาที่ต้องการโพสต์ (เป็น List ของชั่วโมง)
post_hours = [10, 14, 20]  # โพสต์ 10 โมง, บ่าย 2, 2 ทุ่ม

def should_post_now():
    """เช็กว่าตอนนี้ตรงกับเวลาที่ตั้งไว้หรือเปล่า"""
    current_hour = datetime.now().hour
    return current_hour in post_hours

while True:
    if should_post_now():
        selected_message = random.choice(messages)
        selected_group = random.choice(group_ids)

        try:
            bot.send_message(chat_id=selected_group, text=selected_message, parse_mode=telegram.constants.ParseMode.HTML)
            print(f"✅ ส่งข้อความสำเร็จ: {selected_message} -> {selected_group}")
        except Exception as e:
            print(f"❌ ส่งไม่สำเร็จ: {e}")

        time.sleep(3700)  # รอ 1 ชม.ก่อนยิงใหม่ เพื่อกันยิงซ้ำภายในชั่วโมงเดียว
    else:
        print("⌛ รอถึงรอบโพสต์ถัดไป...")
        time.sleep(600)  # เช็กทุกๆ 10 นาที
