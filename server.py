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
    response(request.form["from"], "Yes I have recieved you message")
    return "Success", 201

SANDBOX_API_KEY ="6472b4a2614c40222d035bd83f52c576376441eb2c2adf00fe90276b9ec9c709"

def response(recipient_phone_number, message):
    response = requests.post(
        "https://api.africastalking.com/version1/messaging",
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
    
