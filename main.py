#!/bin/python3

import requests

print(requests.__version__)

response = requests.get("http://www.google.com/")
print(response.text)
print(response.status_code)
