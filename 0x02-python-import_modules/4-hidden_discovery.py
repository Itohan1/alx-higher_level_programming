#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_fun = dir()
    for i in range(0, len(all_fun)):
        if all_fun[i][:2] != "__":
            print("{:s}".format(all_fun[i]))
