#!/usr/bin/python3
"""returns True if the object is an instance"""


def is_kind_of_class(obj, a_class):
    """def is_kind_of_class(obj, a_class)"""

    if isinstance(obj, a_class):
        return (True)
    return (False)
