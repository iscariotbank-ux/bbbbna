from zoneinfo import ZoneInfo

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

# ดึงโพสต์ล่าสุด 1 โพสต์
medias = cl.user_medias(user_id, amount=1)
media = medias[0]

# print media ID ของโพสต์
print("Media ID:", media.pk)

# แปลง timestamp (taken_at) เป็นเวลาประเทศไทย แล้ว print ออกมา
taken_at_th = media.taken_at.astimezone(ZoneInfo("Asia/Bangkok"))
print("Taken at (Thailand):", taken_at_th.strftime("%Y-%m-%d %H:%M:%S %Z"))
