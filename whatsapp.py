from twilio.rest import Client

account_sid='AC3855731d589c1e2cec6d427eef24822e'
auth_token='f6ae00d075d1acab8e84cf50e1aee105'
client = Client(account_sid, auth_token)

from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:+2348102186232'

account = client.api.accounts('AC3855731d589c1e2cec6d427eef24822e').update(
                                                                status='active'
                                                            )
print(account.friendly_name)

