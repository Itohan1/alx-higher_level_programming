#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL"""


import requests
import sys

if __name__ == "__main__":
    """Write a Python script that takes in a URL, sends a request to the URL"""
    response = requests.get(sys.argv[1])
    if response.status_code == 200:
        response_id = response.headers.get('X-Request-Id')
        print(response_id)
