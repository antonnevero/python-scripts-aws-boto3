import requests
import smtplib
import os
import paramiko
import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


def send_notification(email_msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f'Subject: SITE DOWN\n{email_msg}'
        smtp.sendmail(EMAIL_ADDRESS, 'nevero.anton@gmail.com', message)

def monitor_app():
    try:
        response = requests.get('http://35.158.218.87/')
        if response.status_code == 200:
            print("Application is running successfully")
        else:
            print("Application Down, Fix it!")
            msg = f"Application returned {response.status_code}"
            send_notification(msg)

            # restart the app
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('host???', username='root', key_filename='/home/.../.ssh/id_rsa')
            stdin, stdout, stderr = ssh.exec_command('docker start #of_container')
            print(stdout.readlines())
            ssh.close()
            print('Application started')
    except Exception as ex:
        print(f"Connection error happened: {ex}")
        msg = 'Subject: SITE DOWN\nApp not accessible at all!'
        send_notification(msg)


schedule.every(5).minutes.do(monitor_app)

while True:
    schedule.run_pending()
