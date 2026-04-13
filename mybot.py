import telebot

# کلیلە تایبەتەکەی تۆ
API_TOKEN = '8789899823:AAGvLBJSYu6996tx_IzXAl8C59X_l3JXFPM'
bot = telebot.TeleBot(API_TOKEN)

# وەڵامدانەوەی فەرمانی Start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "سڵاو فەرماندە! 🦾\n\n"
        "من بۆتی پارێزەری تۆم. سیستەمەکە ئێستا لەسەر سێرڤەرەکەت چالاکە.\n"
        "ئامادەم بۆ پاراستنی گروپەکان لە سپام و لێنک."
    )
    bot.reply_to(message, welcome_text)

# پاراستنی گروپ: سڕینەوەی لێنکی ڕیکلام
@bot.message_handler(func=lambda message: "http" in message.text or "t.me" in message.text)
def delete_links(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"⚠️ بەڕێز {message.from_user.first_name}، ناردنی لێنک و ڕیکلام لێرە قەدەغەیە!")
    except:
        print("بۆتەکە پێویستی بە دەسەڵاتی ئادمینە بۆ سڕینەوەی نامە.")

print("بۆتەکە ئێستا بە سەرکەوتوویی کار دەکات... 🚀")
bot.polling()
