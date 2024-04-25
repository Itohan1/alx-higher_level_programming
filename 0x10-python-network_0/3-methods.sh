#!/usr/bin/bash
# takes in a URL and displays all HTTP methods the server will accept

curl -sI -X OPTIONS "$1" | grep "Allow" | sed 's/Allow: //' | tr -d '\n'
