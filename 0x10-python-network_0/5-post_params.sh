#!/bin/bash
# Write a Bash script that takes in a URL, sends a POST request to the passed URL
subject="I will always be here for PLD"; email="test@gmail.com"; curl -X POST -s -d "email=$email&subject=$subject" "$1"
