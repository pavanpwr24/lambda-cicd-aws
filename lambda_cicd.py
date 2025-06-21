import json
import pandas as pd
import requests

def lambda_function(event,context):
    print("event",event)
    response=requests.get("https://www.google.com/")
    print(response.text)
    d1={"col1":[3,5],"col2":[8,9]}
    df=pd.DataFrame(data=d1)
    print(df)


