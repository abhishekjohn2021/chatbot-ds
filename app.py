from flask import Flask, request, jsonify
import joblib

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
app = Flask(__name__)

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
    app.run(debug=True)
