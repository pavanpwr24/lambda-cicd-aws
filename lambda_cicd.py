import json
import requests

def lambda_function(event,context):
    print("event",event)
    response=requests.get("https://www.google.com/")
    print(response.text)


