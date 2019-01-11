#!/bin/python3

import requests

print("requests version: " + requests.__version__)
response = requests.get("https://raw.githubusercontent.com/skywolff/CMPUT404-lab01/master/main.py")
with open("downloadededScript.py", "w") as f:
    f.write(response.text)
print(response.text)
