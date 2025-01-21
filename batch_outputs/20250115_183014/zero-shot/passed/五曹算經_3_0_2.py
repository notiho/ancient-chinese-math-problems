"""
今有粟七百五十斛。問：為糲米㡬何？
術曰：列粟七百五十斛，以三十乘之得二萬二千五百斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the value of "a" (the amount of 糲米 in 斛). Here's the solution:


"""


from fractions import Fraction

# Given values
粟 = 750  # 粟 in 斛
multiplier = 30
divisor = 50

# Calculation
a = Fraction(粟 * multiplier, divisor)

# Result
a  # a is the amount of 糲米 in 斛


"""


The value of `a` will be the solution in terms of 斛.
"""


"""
"""
