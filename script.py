from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    phone_numbers = request.form.getlist('phone_numbers')
    message_body = 'Hej, detta är ett test-SMS från Marcus och Tommy!'
    account_sid = 'ACd7401dc46709cf949a6d6b0093a1bf24'
    auth_token = '6b8f43cb40a2a133eb5fc6e63e4edc2f'
    twilio_phone_number = '+12518423747'
    client = Client(account_sid, auth_token)
    for phone_number in phone_numbers:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=phone_number
        )
        print(f"SMS skickat till {phone_number}. SID: {message.sid}")
    return "SMS sent!"

    dflkjdflkdf

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)