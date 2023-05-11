import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


response = requests.get('http://35.158.218.87/')
if response.status_code == 200:
    print("Application is running successfully")
else:
    print("Application Down, Fix it!")
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)