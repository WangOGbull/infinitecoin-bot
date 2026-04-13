import os
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import threading
import asyncio

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
        "👇 *Tap below to launch the game* 👇",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎮 PLAY NOW", web_app={"url": GAME_URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎮 *Launch Infinitecoin Jumper* 🎮\n\nTap the button below.",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *GAME CONTROLS* 📖\n\n"
        "✦ JUMP: Tap ♾️ button or SPACE/UP arrow\n"
        "✦ DOUBLE JUMP: Tap again in air\n"
        "✦ COLLECT: ♾️ IFC coins (5-100 IFC)\n"
        "✦ AVOID: Red viruses (-10% health) | Black viruses (-30% health)\n"
        "✦ GIFT BOX: +10,000 IFC\n"
        "✦ DAILY BONUS: +500 IFC every 24 hours",
        parse_mode="Markdown"
    )

async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔧 *SMART CONTRACT DEPLOYMENT SOON* 🔧\n\n"
        "Real IFC wallet connection and payouts coming soon.",
        parse_mode="Markdown"
    )

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("wallet", wallet))
    
    application.run_polling()

if __name__ == "__main__":
    # Run bot in background
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    
    # Run Flask
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
