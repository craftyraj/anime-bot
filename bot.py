import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8780425601:AAFUWTh4exyStxtN5I26uawerrFKXmVVNAg"

bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎬 Anime Library", "👤 Profile")
    markup.add("💰 Add Balance", "📦 My Purchases")
    markup.add("🎁 Referral", "🎡 Lucky Spin")
    markup.add("🆘 Support")
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥 Welcome to Anime World Store",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda m: True)
def menu(message):

    if message.text == "🎬 Anime Library":
        bot.send_message(message.chat.id, "Anime list coming soon...")

    elif message.text == "👤 Profile":
        bot.send_message(message.chat.id, f"User ID: {message.from_user.id}")

    elif message.text == "💰 Add Balance":
        bot.send_message(message.chat.id, "UPI payment coming soon")

    elif message.text == "📦 My Purchases":
        bot.send_message(message.chat.id, "You haven't purchased anything yet")

    elif message.text == "🎁 Referral":
        bot.send_message(message.chat.id, "Referral system coming soon")

    elif message.text == "🎡 Lucky Spin":
        bot.send_message(message.chat.id, "Spin feature coming soon")

    elif message.text == "🆘 Support":
        bot.send_message(message.chat.id, "Contact admin: @yourusername")


bot.infinity_polling()