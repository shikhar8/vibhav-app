from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8fcac2d7dc5128249d984acaec5d41ea"
# Your Auth Token from twilio.com/console
auth_token  = "51d5944f42b084edad42f341762f9f85"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918544235460",
    from_="+17372041894",
    body="Hello from Python!")

print(message.sid)