from flask import Flask, request, jsonify, render_template
import joblib
import os

# Load ML model
model = joblib.load('intent_model.pkl')

# Intent to response mapping
responses = {
    "greeting": ["Hi! How can I assist you?"],
    "thanks": ["You're welcome!"],
    "goodbye": ["Goodbye and have a great day!"],
    "return_policy": ["You can return items within 30 days of purchase."],
    "order_status": ["Please provide your order ID to check the status."],
    "unknown": ["Sorry, I didn't understand that. Can you rephrase?"]
}

# Initialize Flask app
app = Flask(__name__)\

@app.route('/')
def home():
    return render_template("index.html")  # 👈 serve the chat UI

def get_bot_reply(message):
    if "hello" in message.lower():
        return "Hi! How can I help you?"
    else:
        return "I'm not sure what you mean."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    try:
        intent = model.predict([user_input])[0]
    except:
        intent = "unknown"
    response = responses.get(intent, responses["unknown"])
    return jsonify({"response": response[0]})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT if available
    app.run(host='0.0.0.0', port=port, debug=True)




