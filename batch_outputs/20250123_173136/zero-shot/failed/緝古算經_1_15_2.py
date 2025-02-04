"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. Here's the solution:


"""


from fractions import Fraction
from math import pow

# Given values
m = Fraction(4036, 5)  # 冪四千三十六五分之
s = Fraction(1, 65)    # 股少於弦六五分之一

# Step 1: 冪自乘，倍少數而一，為實
real = m * m * (2 * s + 1)

# Step 2: 半少，為廉法，從
half_s = s / 2

# Step 3: 開立方除之，即股
g = pow(real, 1/3) / (1 + half_s)

# Step 4: 加差，即弦
a = g + g * s

# Result
a


"""


The variable `a` will contain the value of the hypotenuse (弦).
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 88.2423813618962"""
