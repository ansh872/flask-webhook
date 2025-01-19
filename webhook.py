from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Log headers and raw body
        print(f"Headers: {request.headers}")
        print(f"Raw Body: {request.data.decode('utf-8')}")

        # Parse JSON body
        data = request.json
        if not data:
            print("Invalid or missing JSON body")
            return jsonify({"error": "Invalid or missing JSON body"}), 400
        
        # Log parsed JSON data
        print(f"Parsed JSON Data: {data}")
        
        return jsonify({"message": "Webhook received successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)