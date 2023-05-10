import requests

response = requests.get('http://35.158.218.87/')
print(response.status_code)