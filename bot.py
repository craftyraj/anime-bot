from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8780425601:AAFUWTh4exyStxtN5I26uawerrFKXmVVNAg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.first_name

    keyboard = [
        ["🛍 Shop Anime"],
        ["📦 My Library", "👤 Profile"],
        ["💰 Add Balance", "🎁 Referral"],
        ["🎰 Lucky Spin"],
        ["🆘 Support"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    text = f"""
🎌 *ANIME STREAMING STORE*

👋 Welcome *{user}*

⭐ *FEATURES*

🎬 Full Anime Season Access
📺 Watch All Episodes Anytime
⚡ Instant Access After Payment
🔒 Secure Payment System
🎁 Referral Rewards
🏆 24/7 Support

🚀 Click *Shop Anime* to explore anime library!
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
