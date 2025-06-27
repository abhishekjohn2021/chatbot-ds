


from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Replace this with your real bot logic
def get_bot_reply(message):
    if "hello" in message.lower():
        return "Hi! How can I help you?"
    else:
        return "I'm not sure what you mean."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    reply = get_bot_reply(user_input)
    return jsonify({'response': reply})

# 🆕 Webhook route for Telegram
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        response = get_bot_reply(text)

        send_message(chat_id, response)

    return jsonify({'ok': True})

def send_message(chat_id, text):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{7868342948:AAFSdg_j1tkN9jbGcDD8TEN4Y0hT3HYrJEA}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run()


