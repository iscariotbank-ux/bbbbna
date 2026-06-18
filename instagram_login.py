from instagrapi import Client

# กำหนด username และ password ของบัญชี Instagram
USERNAME = "your_username"
PASSWORD = "your_password"

# สร้าง Client
cl = Client()

# ล็อกอินเข้าบัญชี Instagram
cl.login(USERNAME, PASSWORD)

# print ข้อความเมื่อล็อกอินสำเร็จ
print("Login OK")
