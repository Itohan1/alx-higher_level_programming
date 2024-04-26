#!/bin/bash
# Write a Bash script that takes in a URL as an argument
curl -s -H "X-School-User-Id: 98" "$1" ; echo -n "Hello School!"
