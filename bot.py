import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = "8695754535:AAF3WjpAdQmmRWXqubN6oSidYYGmQEdr_ek"
GAME_URL = "https://infinitecoin-jumper-s59b.vercel.app"

API_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def health():
    return "Bot is running", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        
        if text == '/start':
            send_start_message(chat_id)
        elif text == '/play':
            send_play_message(chat_id)
        elif text == '/help':
            send_help_message(chat_id)
        elif text == '/wallet':
            send_wallet_message(chat_id)
    
    return jsonify({"status": "ok"}), 200

def send_start_message(chat_id):
    keyboard = {
        "inline_keyboard": [[{
            "text": "🎮 PLAY INFINITE JUMPER",
            "web_app": {"url": GAME_URL}
        }]]
    }
    payload = {
        "chat_id": chat_id,
        "text": "🚀 *INFINITE JUMPER* 🚀\n\nTap the button to play and earn IFC.",
        "reply_markup": keyboard,
        "parse_mode": "Markdown"
    }
    requests.post(f"{API_URL}/sendMessage", json=payload)

def send_play_message(chat_id):
    keyboard = {
        "inline_keyboard": [[{
            "text": "🎮 PLAY NOW",
            "web_app": {"url": GAME_URL}
        }]]
    }
    payload = {
        "chat_id": chat_id,
        "text": "🎮 *Launch Infinitecoin Jumper* 🎮\n\nTap the button to start playing.",
        "reply_markup": keyboard,
        "parse_mode": "Markdown"
    }
    requests.post(f"{API_URL}/sendMessage", json=payload)

def send_help_message(chat_id):
    payload = {
        "chat_id": chat_id,
        "text": "📖 *GAME CONTROLS* 📖\n\n"
        "✦ JUMP: Tap the ♾️ button or press SPACE/UP arrow\n"
        "✦ DOUBLE JUMP: Tap again in the air\n"
        "✦ COLLECT: ♾️ IFC coins (5-100 IFC)\n"
        "✦ AVOID: Red viruses (-10% health)\n"
        "✦ AVOID: Black viruses (-30% health)\n"
        "✦ GIFT BOX: +10,000 IFC after dodging 25 viruses\n"
        "✦ DAILY BONUS: +500 IFC every 24 hours\n\n"
        "🔧 Smart contract coming soon for real IFC payouts!",
        "parse_mode": "Markdown"
    }
    requests.post(f"{API_URL}/sendMessage", json=payload)

def send_wallet_message(chat_id):
    payload = {
        "chat_id": chat_id,
        "text": "🔧 *SMART CONTRACT DEPLOYMENT SOON* 🔧\n\n"
        "Real IFC wallet connection and payouts will be available after the smart contract is deployed.\n\n"
        "Stay tuned for updates!",
        "parse_mode": "Markdown"
    }
    requests.post(f"{API_URL}/sendMessage", json=payload)

def set_webhook():
    webhook_url = f"https://infinitecoin-bot.onrender.com/webhook"
    response = requests.post(f"{API_URL}/setWebhook", json={"url": webhook_url})
    print("Webhook response:", response.json())

if __name__ == "__main__":
    set_webhook()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
