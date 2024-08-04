import pywhatkit.whats

# Specify the phone number (with country code) and the message
phone_number = "+919601397062"
message = "Hello from Python! This is an instant WhatsApp message."

# Send the message instantly
pywhatkit.whats.sendwhatmsg_instantly(phone_number, message)

# pywhatkit.whats.sendwhatmsg(phone_number, message,0,0,True)


