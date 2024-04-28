#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL"""


import urllib.request
import sys

if __name__ == "__main__":
    """Write a Python script that takes in a URL, sends a request to the URL"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        response_id = response.headers.get('X-Request-Id')
        print(response_id)
