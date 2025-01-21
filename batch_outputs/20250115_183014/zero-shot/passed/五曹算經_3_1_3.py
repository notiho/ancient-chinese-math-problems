"""
今有粟二百九十斛。問：為粺米㡬何？
術曰：列粟二百九十斛，以二十七乘之得七千八百三十斛，以五十除之即得。
答曰： a斛 。
"""

"""
To translate the ancient Chinese math problem into Python code, we will compute the value of the unknown `a` using the given operations. Here's the solution:


"""


from fractions import Fraction

# Given data
粟 = 290  # in 斛
乘數 = 27
除數 = 50

# Calculation
a = Fraction(粟 * 乘數, 除數)

# Result
a  # in 斛


"""


The value of `a` will be stored as a `Fraction` representing the number of 斛 (a unit of volume).
"""


"""
"""
