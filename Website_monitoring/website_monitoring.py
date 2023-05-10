import requests

response = requests.get('http://35.158.218.87/')
if response.status_code == 200:
    print("Application is running successfully")
else:
    print("Application Down, Fix it!")