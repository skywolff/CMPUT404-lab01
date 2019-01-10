#!/bin/python3
import requests
print("requests version: " + requests.__version__)
print(requests.get("http://www.google.com/").text)
