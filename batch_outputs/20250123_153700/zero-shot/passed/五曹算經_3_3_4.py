"""
今有粟三百六十二斛。問：為御米㡬何？
術曰：列粟三百六十二斛，以二十一升乘之得七千六百二斛，以五十除之即得。
答曰： a斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
粟 = 362  # 粟 in 斛
升_per_斛 = 21  # 21 升 per 斛
升_per_御米 = 50  # 50 升 per 御米

# Calculation
a = Fraction(粟 * 升_per_斛, 升_per_御米)  # a in 斛 (御米)

# Result
a


"""


The variable `a` will contain the result in terms of 御米 (斛).
"""


"""
"""
