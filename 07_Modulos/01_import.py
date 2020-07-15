import math

print(math.factorial(6))  # 720

from math import factorial as fat

print(fat(8)) # 40320

help(math)
"""
NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
"""
help(math.log)
"""
log(...)
    log(x, [base=math.e])
    Return the logarithm of x to the given base.
    
    If the base not specified, returns the natural logarithm (base e) of x.
"""