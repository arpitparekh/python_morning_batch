# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Email configuration
# sender_email = "arpitparekh9@gmail.com"
# receiver_email = "namratapandya26@gmail.com"
# password = "iitrydlyibfgaxrb"
# smtp_server = "smtp.gmail.com"
# port = 587  # For starttls

# # Create message
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = receiver_email
# message["Subject"] = "Test email from Python"

# # Add body to email
# body = "This is a test email sent from Python using smtplib."
# message.attach(MIMEText(body, "plain"))

# # Create SMTP session
# try:
#     with smtplib.SMTP(smtp_server, port) as server:
#         server.starttls()  # Secure the connection
#         server.login(sender_email, password)
#         server.send_message(message)
#     print("Email sent successfully")
# except Exception as e:
#     print(f"Error: {e}")
    
    
import smtplib

def sendMail(sender,receiver,password,message):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(sender, password)
    # sending the mail
    s.sendmail(sender, receiver, message)
    # terminating the session
    s.quit()    
    
# iitrydlyibfgaxrb    
    