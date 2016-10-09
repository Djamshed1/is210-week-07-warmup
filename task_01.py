#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week 7 task 1"""

def fibonacci(maxint):
    """Fibonacci function that prints a maximum value

    Args:
        maxint(int): an integer that will serve as the upper bound of the loop.

    Returns:
        list: a Fibonacci numbers.

    Examples:
        >>> import task_01
        >>> task_01.fibonacci(11)
        [0, 1, 1, 2, 3, 5, 8]
        >>> task_01.fibonacci(20)
        [0, 1, 1, 2, 3, 5, 8, 13]
        """
    flist = []
    a, b = 0, 1
    count = maxint
    while b < count:
        flist.append(a)
        a, b = b, a+b
        count += 1
    return flist
