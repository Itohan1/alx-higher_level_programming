#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sIL "$1" | grep -q "HTTP/1.1 200 OK" && curl -sL "$1"
