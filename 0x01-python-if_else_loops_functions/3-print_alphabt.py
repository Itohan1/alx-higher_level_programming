#!/usr/bin/python3
for j in range(97, 123):
    if j in [101, 113]:
        continue
    print("{}".format(chr(j)), end='')
