#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email"""
import sys
import requests

if __name__ == "__main__":
    """Write a Python script that takes in a URL and an email"""
    req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    if req.status_code == 200:
        print(f"Your email is: {req.text}")
