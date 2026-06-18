from instagrapi import Client

# instagrapi Client ที่ล็อกอินแล้ว (กำหนด/ล็อกอินจากภายนอกก่อนเรียกใช้ฟังก์ชัน)
client = Client()


def post_comment(media_id, text):
    """ส่งคอมเมนต์ไปยังโพสต์ที่ระบุด้วย instagrapi

    Args:
        media_id: media ID ของโพสต์ที่ต้องการคอมเมนต์
        text: ข้อความคอมเมนต์
    """
    try:
        # ส่งคอมเมนต์ไปยังโพสต์
        client.media_comment(media_id, text)
        print("คอมเมนต์สำเร็จ:", text)
    except Exception as e:
        print("คอมเมนต์ไม่สำเร็จ เกิดข้อผิดพลาด:", e)
