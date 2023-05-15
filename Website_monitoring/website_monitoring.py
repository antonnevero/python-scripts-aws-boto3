import requests
import smtplib
import os
import paramiko

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


def send_notification(email_msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f'Subject: SITE DOWN\n{email_msg}'
        smtp.sendmail(EMAIL_ADDRESS, 'nevero.anton@gmail.com', message)


try:
    response = requests.get('http://35.158.218.87/')
    if response.status_code == 200:
        print("Application is running successfully")
    else:
        print("Application Down, Fix it!")
        msg = f"Application returned {response.status_code}"
        send_notification(msg)

        ssh = paramiko.SSHClient()
        ssh.connect('host', )
except Exception as ex:
    print(f"Connection error happened: {ex}")
    msg = 'Subject: SITE DOWN\nApp not accessible at all!'
    send_notification(msg)
