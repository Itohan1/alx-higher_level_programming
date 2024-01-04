#!/usr/bin/python3
for j in range(0, 100):
    if j == 99:
        print(f"{j}")
    else:
        print("{:02d}, ".format(j), end='')
