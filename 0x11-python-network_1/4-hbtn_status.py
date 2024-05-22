#!/usr/bin/python3
"""Write a Python script that fetches"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    body = requests.get(url)
    if body.status_code == 200:
        print("Body response:")
        print(f"\t - type: {type(body.text)}")
        print(f"\t - content: {body.text}")
