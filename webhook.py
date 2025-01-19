from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Log the incoming request headers and body
        print(f"Headers: {request.headers}")
        print(f"Body: {request.data}")
        
        # Parse JSON body
        data = request.json
        if not data:
            return jsonify({"error": "Invalid or missing JSON body"}), 400
        
        # Log the parsed JSON data
        print(f"Parsed JSON Data: {data}")
        
        return jsonify({"message": "Webhook received successfully!"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Something went wrong"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)