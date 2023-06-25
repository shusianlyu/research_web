import smtplib
import ssl
import app_password


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # replace username
    username = "shusianlyu@gmail.com"
    password = app_password.APP_PASSWORD

    # replace receiver
    receiver = "shusianlyu@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
