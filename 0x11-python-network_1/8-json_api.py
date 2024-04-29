#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    response = requests.post(url, data={'q': q})
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                print("[{}] {}".format(data.get('id'), data.get('name')))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print(f"Error code: {response.status_code}")
