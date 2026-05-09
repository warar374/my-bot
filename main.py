import telebot
from g4f.client import Client
import os
5146231674:AAGRdCMYL9Ayy3bM1LCaDRkvqtHsLkQTII8"
bot = telebot.TeleBot(TOKEN)
client = Client()

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}],
        )
        bot.reply_to(message, response.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    bot.infinity_polling()
