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

@app.route(f'/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        
        if text == '/start':
            send_start_message(chat_id)
    
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

def set_webhook():
    webhook_url = f"https://infinitecoin-bot.onrender.com/webhook"
    response = requests.post(f"{API_URL}/setWebhook", json={"url": webhook_url})
    print("Webhook response:", response.json())

if __name__ == "__main__":
    set_webhook()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
