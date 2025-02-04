"""
假令有句股相乘冪四千三十六五分之□，股少於弦六五分之一。問：弦多少？。
術曰：冪自乘，倍少數而一，為實。半少，為廉法，從。開立方除之，即股。加差，即弦。
答曰：弦 a 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
mian = Fraction(4036, 5)  # 冪四千三十六五分之□
cha = Fraction(1, 5)      # 股少於弦六五分之一

# Step 1: 冪自乘，倍少數而一，為實。
shi = mian * mian * (cha * 2 + 1)

# Step 2: 半少，為廉法，從。
lianfa = cha / 2

# Step 3: 開立方除之，即股。
gu = shi ** (1/3) / lianfa

# Step 4: 加差，即弦。
a = gu + cha

# The result is stored in variable `a`


"""
 

The variable `a` now contains the value of the unknown "弦".
"""


"""
Variable 'a' has wrong value. Expected: 1147/10, Actual: 970.0326051168893"""
