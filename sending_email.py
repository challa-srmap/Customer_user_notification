import smtplib
from email.mime.text import MIMEText
def send(email_sender,email_password, recipients_list,message,subject):
    # Connecting to the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)  #smtp server of gmail
    server.starttls()
    server.login(email_sender, email_password)

    for recipient in recipients_list: # Sending the email to each recipient
        email = MIMEText(message)
        email["From"] = email_sender
        email["To"] = recipient
        email["Subject"] = subject
        server.send_message(email)

    server.quit()

