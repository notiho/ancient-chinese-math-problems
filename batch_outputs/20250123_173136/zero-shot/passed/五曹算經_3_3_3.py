"""
今有粟三百六十二斛。問：為御米㡬何？
術曰：列粟三百六十二斛，以二十一升乘之得七千六百二斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves converting 362斛 of 粟 into 御米 using the given method.

Here is the Python code:


"""


from fractions import Fraction

# Given values
粟 = 362  # in 斛
conversion_factor = Fraction(21, 50)  # 21升 per 50 units

# Calculation
a = 粟 * conversion_factor  # Result in 斛

# Output the result
a  # This is the answer in 斛


"""


The variable `a` will hold the solution in 斛.
"""


"""
"""
