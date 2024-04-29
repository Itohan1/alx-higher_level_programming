#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    """Write a Python script that takes in a URL and an email"""

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    req = urllib.request.Request(sys.argv[1], data, method="POST")
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(f"Your email is: {body}")
