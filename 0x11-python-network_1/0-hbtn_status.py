#!/usr/bin/python3
import urllib.request
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()

        print("Body_response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- content:", html.decode('utf-8'))
