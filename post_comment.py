def post_comment(client, media_id, text):
    """ส่งคอมเมนต์ไปยังโพสต์ที่ระบุด้วย instagrapi

    Args:
        client: instagrapi Client ที่ล็อกอินแล้ว
        media_id: media ID ของโพสต์ที่ต้องการคอมเมนต์
        text: ข้อความคอมเมนต์
    """
    try:
        # ส่งคอมเมนต์ไปยังโพสต์
        client.media_comment(media_id, text)
        print("คอมเมนต์สำเร็จ:", text)
        return True
    except Exception as e:
        print("คอมเมนต์ไม่สำเร็จ เกิดข้อผิดพลาด:", e)
        return False
