import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
import threading

# YOUR NEW BOT TOKEN - HARDCODED
TOKEN = "8695754535:AAF3WjpAdQmmRWXqubN6oSidYYGmQEdr_ek"
GAME_URL = "https://infinitecoin-jumper-s59b.vercel.app"

app = Flask(__name__)

@app.route('/')
def health():
    return "Bot is running", 200

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎮 PLAY INFINITE JUMPER", web_app={"url": GAME_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🚀 *INFINITE JUMPER* 🚀\n\n"
        "Jump, collect ♾️ IFC, avoid viruses, and earn rewards.\n\n"
        "✦ Double jump in air\n"
        "✦ Dodge red viruses (-10% health)\n"
        "✦ Dodge black viruses (-30% health)\n"
        "✦ Collect gift boxes (+10,000 IFC)\n"
        "✦ Daily bonus every 24 hours\n\n"
        "👇 *Tap below to launch the game* 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎮 PLAY NOW", web_app={"url": GAME_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎮 *Launch Infinitecoin Jumper* 🎮\n\nTap the button below to start playing.",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *GAME CONTROLS* 📖\n\n"
        "✦ JUMP: Tap the ♾️ button or press SPACE/UP arrow\n"
        "✦ DOUBLE JUMP: Tap again in the air\n"
        "✦ COLLECT: ♾️ IFC coins (5-100 IFC)\n"
        "✦ AVOID: Red viruses (-10% health)\n"
        "✦ AVOID: Black viruses (-30% health)\n"
        "✦ GIFT BOX: +10,000 IFC after dodging 25 viruses\n"
        "✦ DAILY BONUS: +500 IFC every 24 hours\n\n"
        "🔧 Smart contract coming soon for real IFC payouts!",
        parse_mode="Markdown"
    )

async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔧 *SMART CONTRACT DEPLOYMENT SOON* 🔧\n\n"
        "Real IFC wallet connection and payouts will be available after the smart contract is deployed.\n\n"
        "Stay tuned for updates!",
        parse_mode="Markdown"
    )

def run_bot():
    bot_app = Application.builder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CommandHandler("play", play))
    bot_app.add_handler(CommandHandler("help", help_command))
    bot_app.add_handler(CommandHandler("wallet", wallet))
    bot_app.run_polling()

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    run_flask()
