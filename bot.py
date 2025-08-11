import telebot

# Replace 'YOUR_BOT_TOKEN' with the token you get from BotFather
BOT_TOKEN = '8430732004:AAHmY0_-nFsVoXsU7PT3CmVU63zjcgI9g6M'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm a simple bot. Send me any message and I'll echo it!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()
