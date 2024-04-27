#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Write a function that finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return (None)
    peak = list_of_integers[0]
    i = 1

    while i < len(list_of_integers):
        if peak < list_of_integers[i]:
            peak = list_of_integers[i]
        i += 1
    return (peak)
