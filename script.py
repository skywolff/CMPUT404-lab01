#!/bin/python3
import requests

print("requests version: " + requests.__version__)
print(requests.get("http://www.google.com/").text)
response = requests.get("https://raw.githubusercontent.com/skywolff/CMPUT404-lab01/master/getGoogle.py")
with open("downloadededScript.py", "w") as f:
    f.write(response.text)
print(response.text)
