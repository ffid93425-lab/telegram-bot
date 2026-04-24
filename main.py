import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['anouce'])
def announce(message):

    # Only work in DM
    if message.chat.type != "private":
        return

    if not message.reply_to_message:
        bot.reply_to(message, "❌ Reply to message first.")
        return

    args = message.text.split()

    if len(args) < 2:
        bot.reply_to(message, "❌ Use:\n/anouce https://t.me/channelusername")
        return

    try:
        chat_username = "@" + args[1].split("t.me/")[1]

        # ✅ COPY instead of forward
        bot.copy_message(
            chat_id=chat_username,
            from_chat_id=message.reply_to_message.chat.id,
            message_id=message.reply_to_message.message_id
        )

        bot.reply_to(message, "✅ Sent Successfully")

    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()
