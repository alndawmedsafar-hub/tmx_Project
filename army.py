import threading

def attack_from_combo(bot_id, combo_list):
    # هەر بۆتێک بەشێکی لیستەکە دەبات
    for account in combo_list:
        email, password = account.split(":")
        
        # لێرەدا بۆتەکە هێرش دەکات
        print(f"🚀 بۆتی {bot_id} تاقی دەکاتەوە: {email} | {password}")
        
        # ئەگەر سەرکەوتوو بوو، لە فایلی 'cracked_passwords.txt' سەیڤی دەکات
        # (لێرەدا کۆدی Requests دادەنرێت بۆ لۆگین)

# خوێندنەوەی فایلی کۆمبۆ کە دروستت کردووە
with open("combo.txt", "r") as f:
    all_accounts = f.readlines()

# دابەشکردنی ١٠٠ بۆتەکە
for i in range(100):
    # دابەشکردنی لیستەکە بۆ ١٠٠ بەش
    part = all_accounts[i::100]
    threading.Thread(target=attack_from_combo, args=(i, part)).start()
