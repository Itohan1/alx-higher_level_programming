#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    try:
        req = sys.argv[1]
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
