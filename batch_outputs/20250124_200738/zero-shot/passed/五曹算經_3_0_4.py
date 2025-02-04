"""
今有粟七百五十斛。問：為糲米㡬何？
術曰：列粟七百五十斛，以三十乘之得二萬二千五百斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
粟 = 750  # in 斛
multiplier = 30
divisor = 50

# Calculation
a = Fraction(粟 * multiplier, divisor)

# Result
a  # in 斛
#----- content ends here -----


"""


The variable `a` will hold the value of the answer in 斛.
"""


"""
"""
