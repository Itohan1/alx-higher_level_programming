#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL"""
import requests
import sys

if __name__ == "__main__":
    req = sys.argv[1]
    body = requests.get(req)
    if body.status_code == 200:
        print(body.text)
    if body.status_code >= 400:
        print(f"Error code: {body.status_code}")
