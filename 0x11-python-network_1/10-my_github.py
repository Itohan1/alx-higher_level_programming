#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials"""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    req = requests.post(url, auth=(sys.argv[1], sys.argv[2]))
    if req.status_code == 200:
        user_info = req.json()
        print(user_info['id'])
    else:
        print(f"Unable to retrive information")
