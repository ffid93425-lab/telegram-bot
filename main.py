import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['anouce'])
def announce(message):

    # ✅ Only allow in private chat (DM)
    if message.chat.type != "private":
        return

    # Must reply to a message
    if not message.reply_to_message:
        bot.reply_to(message, "❌ Reply to message first.")
        return

    args = message.text.split()

    if len(args) < 2:
        bot.reply_to(message, "❌ Use:\n/anouce https://t.me/channelusername")
        return

    try:
        chat_username = "@" + args[1].split("t.me/")[1]

        bot.forward_message(
            chat_username,
            message.reply_to_message.chat.id,
            message.reply_to_message.message_id
        )

        bot.reply_to(message, "✅ Sent Successfully")

    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

bot.infinity_polling()
