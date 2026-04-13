import os
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8695754535:AAF3WjpAdQmmRWXqubN6oSidYYGmQEdr_ek"
GAME_URL = "https://infinitecoin-jumper-s59b.vercel.app"

app = Flask(__name__)

@app.route('/')
def health():
    return "OK", 200

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎮 PLAY INFINITE JUMPER", web_app={"url": GAME_URL})]]
    await update.message.reply_text(
        "🚀 *INFINITE JUMPER* 🚀\n\nTap the button to play and earn IFC.",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    # Start bot in background
    import threading
    import asyncio
    
    def run_bot():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        bot = Application.builder().token(TOKEN).build()
        bot.add_handler(CommandHandler("start", start))
        bot.run_polling()
    
    threading.Thread(target=run_bot, daemon=True).start()
    
    # Start Flask
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
