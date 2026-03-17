import telebot

TOKEN = "8762269299:AAF3B4wbj38wsSQWd15Esd2D1nvpj9pENGU"
ADMIN_ID = 1713138346  # sizning ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    ism = message.from_user.first_name
    bot.send_message(message.chat.id, f'Salom, {ism}! 👋 Savolingizni yozing!')

@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.chat.id == ADMIN_ID:
        # Admin javob yozayapti
        if message.reply_to_message:
            try:
                # Xabar matnidan ID ni olish
                matn = message.reply_to_message.text
                user_id = int(matn.split("ID: ")[1].split("\n")[0].strip())
                bot.send_message(user_id, message.text)
                bot.reply_to(message, '✅ Javob yuborildi!')
            except Exception as e:
                bot.reply_to(message, f'❌ Xatolik: {e}')
        else:
            bot.reply_to(message, '⚠️ Foydalanuvchi xabariga REPLY qiling!')
    else:
        # Foydalanuvchi xabar yozdi
        ism = message.from_user.first_name
        username = f"@{message.from_user.username}" if message.from_user.username else "yo'q"
        bot.send_message(ADMIN_ID,
            f'📨 Yangi xabar!\n'
            f'👤 {ism} ({username})\n'
            f'ID: {message.chat.id}\n'
            f'💬 {message.text}')
        bot.reply_to(message, '✅ Xabaringiz qabul qilindi!')

print("🚀 Bot ishga tushdi...")
bot.polling(none_stop=True)