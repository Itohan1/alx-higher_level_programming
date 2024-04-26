#!/bin/bash
# Write a Bash script that takes in a URL as an argument
response=$(curl -s -H "X-School-User-Id: 98" "$1"); echo -n "Hello School!"; if [ -z "$response" ]; then exit 1; fi
