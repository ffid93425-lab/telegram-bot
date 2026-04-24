import telebot
import os

TOKEN = 8639479910:AAHa46W55joY7ryjx59HayJiJif017ltBaU
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['anouce'])
def announce(message):
    try:
        if not message.reply_to_message:
            bot.reply_to(message, "❌ Reply to message first.")
            return
        
        args = message.text.split()
        if len(args) < 2:
            bot.reply_to(message, "❌ Use:\n/anouce https://t.me/channelusername")
            return
        
        url = args[1]
        chat_username = "@" + url.split("t.me/")[1]

        bot.forward_message(
            chat_username,
            message.reply_to_message.chat.id,
            message.reply_to_message.message_id
        )

        bot.reply_to(message, "✅ Sent Successfully")

    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()
