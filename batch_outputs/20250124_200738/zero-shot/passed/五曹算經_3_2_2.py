"""
今有粟五百六十斛。問：為糳米㡬何？
術曰：列粟五百六十斛，以二十四乘之得一萬三千四百四十斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
粟 = 560  # 粟 in 斛
乘數 = 24  # Multiplier
除數 = 50  # Divisor

# Calculation
a = Fraction(粟 * 乘數, 除數)  # Result in 斛

# a is the answer in 斛
#----- content ends here -----


"""


The variable `a` will hold the result in units of 斛.
"""


"""
"""
