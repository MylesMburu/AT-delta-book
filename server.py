from flask import Flask
from flask import request
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, flask!</p>"

@app.route('/sms_callback', methods=['POST'])
def sms_callback():
    print(request.method)
    print(request.form)
    from_number = request.form["from"]
    incoming_message = request.form["text"].strip().lower() #recieves users text and converts it to lowercase

    if "option1" in incoming_message:
        message = "You have chosen Option 1. Here is the information you requested."
    elif "option2" in incoming_message:
        message = "You have chosen Option 2. Here is the information you requested."
    elif "option3" in incoming_message:
        message = "You have chosen Option 3. Here is the information you requested."
    else:
        message = "Please send a valid option. Available options: Option1, Option2, Option3"

    send_message(from_number, message)
    return "Success", 201

SANDBOX_API_KEY ="6472b4a2614c40222d035bd83f52c576376441eb2c2adf00fe90276b9ec9c709"

def response(recipient_phone_number, message):
    response = requests.post(
        "https://api.sandbox.africastalking.com/version1/messaging",
        data={
            'username': 'sandbox',
            'to': recipient_phone_number,
            'message': message,
            'from': '48448',
        },
        headers={
            'apiKey': SANDBOX_API_KEY,
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    )
    return response

def send_message(recipient_phone_number, message):
    resp = response(recipient_phone_number, message)
    if resp.status_code == 201:
        print("Message sent successfully")
        print(resp.json())
    else:
        print(f"Failed to send message. Status code: {resp.status_code}")
        print(resp.text)

if __name__ == "__main__":
    app.run(debug=True)
