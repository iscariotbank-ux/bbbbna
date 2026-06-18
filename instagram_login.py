import time
from datetime import datetime, timezone

from instagrapi import Client

# กำหนด username และ password ของบัญชี Instagram
USERNAME = "your_username"
PASSWORD = "your_password"

# username ของร้านค้าที่ต้องการดึงโพสต์
TARGET_USERNAME = "ชื่อร้านค้า"

# สร้าง Client
cl = Client()

# ล็อกอินเข้าบัญชี Instagram
cl.login(USERNAME, PASSWORD)

# print ข้อความเมื่อล็อกอินสำเร็จ
print("Login OK")

# ดึง user ID ของร้านค้าจาก username
user_id = cl.user_id_from_username(TARGET_USERNAME)

# วน loop ตรวจสอบโพสต์ล่าสุดทุก 1 วินาที
while True:
    # ดึงโพสต์ล่าสุด 1 โพสต์
    medias = cl.user_medias(user_id, amount=1)
    media = medias[0]

    # คำนวณอายุของโพสต์ = เวลาปัจจุบัน - taken_at (หน่วยเป็นวินาที)
    now = datetime.now(timezone.utc)
    age_seconds = (now - media.taken_at).total_seconds()

    # ถ้าโพสต์อายุน้อยกว่า 60 วินาที ถือว่าเป็นโพสต์ใหม่
    if age_seconds < 60:
        print("เจอโพสต์ใหม่!", "Media ID:", media.pk)
    else:
        print("ยังไม่มีโพสต์ใหม่")

    # รอ 1 วินาทีก่อนตรวจสอบรอบถัดไป
    time.sleep(1)
