from flask import Flask, request, jsonify

app = Flask(__name__)

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data sent to the webhook
    data = request.json
    print("Received Webhook Data:", data)

    # Respond to Contlo to acknowledge receipt
    return jsonify({"message": "Webhook received successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)