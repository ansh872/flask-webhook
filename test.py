import requests

# Replace this with your deployed Render URL
url = "https://flask-webhook-q6ua.onrender.com/webhook"

# Sample data to send to the webhook
payload = {
    "event": "add_to_cart",
    "user": {
        "email": "example_user@example.com",
        "user_id": "12345"
    },
    "properties": {
        "product_id": "56789",
        "price": 499.99,
        "quantity": 1
    }
}

# Send a POST request
response = requests.post(url, json=payload)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response Text:", response.text)