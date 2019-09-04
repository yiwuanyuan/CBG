# (334) 708-3049
# ACa4c01dddc037244a6bbdc4c629a2923d
# b44fff6661d2e633ae536d4f60e17b55

# Download the helper library from https://www.twilio.com/docs/python/install
def send_SMS():
    from twilio.rest import Client

    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACa4c01dddc037244a6bbdc4c629a2923d'
    auth_token = 'b44fff6661d2e633ae536d4f60e17b55'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="https://xy2.cbg.163.com/equip?s=331&eid=201909041100213-331-JNXZUH1F4D9J&o&view_loc=overall_search",
        from_='+13343452980',
        to='+8613145155669'
    )

    print(message.sid)

#授权密码 wang31415926

