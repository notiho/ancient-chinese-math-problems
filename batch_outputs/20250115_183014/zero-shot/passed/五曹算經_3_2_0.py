"""
今有粟五百六十斛。問：為糳米㡬何？
術曰：列粟五百六十斛，以二十四乘之得一萬三千四百四十斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem involves calculating the amount of 糳米 (processed rice) from 粟 (unprocessed grain). Here's the solution:


"""


from fractions import Fraction

# Given values
粟 = 560  # 粟 in 斛
multiplier = 24
divisor = 50

# Calculation
a = Fraction(粟 * multiplier, divisor)

# Result
a  # a is the amount of 糳米 in 斛


"""


The variable `a` will hold the result in terms of 斛.
"""


"""
"""
