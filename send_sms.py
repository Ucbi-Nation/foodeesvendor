# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC48a24afbd9a65f1d837670a9c53bcc45'
auth_token = 'd215ce6ac8ee1c02d6f4c3a4454852a8'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="We have just received your order and your code is ",
                     from_='+18588793696',
                     to='+23408102186232'
                 )

print(message.sid)