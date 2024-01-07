#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argvs = len(argv) - 1
    if argvs < 1:
        print("{} arguments.".format(argvs))
    elif argvs == 1:
        print("{} argument:".format(argvs))
    else:
        print("{} arguments:".format(argvs))

    for i in range(argvs):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
