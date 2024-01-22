#!/usr/python3

def magic_calculation(a, b):
    answer = 0;
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("passed limit")
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return (answer)
