#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 task 02"""

def bool_to_str(bval):
    """With this function we can return truthy or falsy values.

    Args:
        bval(boolean): a boolean or boolean-like value that can be evaluated for
        truthiness or falsiness.

    Returns:
        val: This string shows the value to see if its true or false

    Examples:
        >>> import task_02
        >>> task_02.bool_to_str(True)
        'Yes'
        
        >>> task_02.bool_to_str('')
        'No'
        """
    if bval is True:
        val = 'Yes'
    else:
        val = 'No'
    return val
