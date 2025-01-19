from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Function to save data to Excel
def save_to_excel(data, filename):
    if os.path.exists(filename):
        # Append data to existing file
        existing_data = pd.read_excel(filename)
        new_data = pd.DataFrame(data)
        combined_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        # Create a new file
        combined_data = pd.DataFrame(data)

    combined_data.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Log headers and raw body
        print("Headers:", request.headers)
        print("Raw Body:", request.data.decode('utf-8'))

        # Parse JSON data
        data = request.json
        if not data:
            print("No JSON data received")
            return jsonify({"error": "Invalid JSON body"}), 400

        print("Parsed JSON Data:", data)

        # Check the event type
        event_type = data.get("event")
        if event_type == "add_to_cart":
            # Extract Add to Cart fields
            add_to_cart_fields = {
                "attribution_automation_id": data.get("attribution_automation_id"),
                "attribution_campaign_id": data.get("attribution_campaign_id"),
                "product_ids": data.get("product_ids"),
                "collection_ids": data.get("collection_ids"),
                "vendor": data.get("vendor"),
                "utm_source": data.get("utm_source"),
                "utm_medium": data.get("utm_medium"),
                "utm_campaign": data.get("utm_campaign"),
                "product_price": data.get("product_price"),
                "sku": data.get("sku"),
                "item_count": data.get("item_count"),
            }
            print("Add to Cart Data:", add_to_cart_fields)

            # Save to Excel
            save_to_excel([add_to_cart_fields], "add_to_cart.xlsx")

        elif event_type == "checkout":
            # Extract Checkout fields
            checkout_fields = {
                "attribution_automation_id": data.get("attribution_automation_id"),
                "attribution_campaign_id": data.get("attribution_campaign_id"),
                "product_ids": data.get("product_ids"),
                "collection_ids": data.get("collection_ids"),
                "item_count": data.get("item_count"),
                "discount_codes": data.get("discount_codes"),
                "shipping_price": data.get("shipping_price"),
                "sku": data.get("sku"),
                "total_price": data.get("total_price"),
                "order_tag": data.get("order_tag"),
                "unique_product_count": data.get("unique_product_count"),
            }
            print("Checkout Data:", checkout_fields)

            # Save to Excel
            save_to_excel([checkout_fields], "checkout.xlsx")

        else:
            print(f"Unknown event type: {event_type}")
            return jsonify({"error": "Unknown event type"}), 400

        return jsonify({"message": "Webhook received successfully!"}), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5001)