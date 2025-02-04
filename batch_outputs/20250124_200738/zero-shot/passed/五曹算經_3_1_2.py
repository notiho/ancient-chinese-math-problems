"""
今有粟二百九十斛。問：為粺米㡬何？
術曰：列粟二百九十斛，以二十七乘之得七千八百三十斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
粟 = 290  # in 斛
乘數 = 27
除數 = 50

# Calculation
a = Fraction(粟 * 乘數, 除數)

# Result
a  # in 斛
#----- content ends here -----


"""


The variable `a` will hold the result in terms of 斛.
"""


"""
"""
