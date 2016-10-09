#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 07 task 03"""

def lexicographics(to_analyze):
    """This function calculates the max, min and average length of words.

    Args:
        to_analyze(str): a string we going to analyze.

    Returns:
        Returns a tuple of max, min and avg counts.

    Examples:
        >>> import task_03
        >>> task_03.lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal('4'))
    
        >>> import data
        >>> task_03.lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))
    """
    import decimal
    
    nlist = to_analyze.split('\n')
    newlist = []
    for item in nlist:
        myvar = len(item.split())
        newlist.append(myvar)
        maxcount = max(newlist)
        mincount = min(newlist)
        average = decimal.Decimal(sum(newlist)/decimal.Decimal(len(nlist)))
    return maxcount, mincount, average
