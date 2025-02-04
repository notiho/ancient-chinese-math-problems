"""
今有田廣一步半、三分步之一。求田一畝，問︰從幾何？
術曰：下有三分，以一為六，半為三，三分之一為二，并之得一十一為法。置田二百四十步，亦以一為六乘之，為實。實如法得從步。
荅曰： a步 。
"""

"""
To solve this problem, we need to compute the value of `a` (in 步, or "steps") based on the given ancient Chinese math problem. Here's the Python code:


"""


from fractions import Fraction

# Given values
田廣 = Fraction(1, 2) + Fraction(1, 3)  # 1/2 + 1/3

# Convert everything to a common denominator (denominator = 6)
田廣 = Fraction(1, 2) * 3 + Fraction(1, 3) * 2  # 3/6 + 2/6 = 11/6
法 = 田廣  # 法 = 11/6

# Total area of the field in 步
田 = 240  # 240 steps

# Convert 240 steps to the same unit as 法 (multiply by 6)
實 = 田 * 6  # 240 * 6 = 1440

# Compute the value of a (steps)
a = 實 / 法  # 1440 / (11/6)

# Simplify the result
a = a  # a = 1440 * 6 / 11 = 8640 / 11

# The result is:
a = Fraction(8640, 11)  # a in 步


"""


The value of `a` is `8640/11` 步.
"""


"""
Variable 'a' has wrong value. Expected: 1440/11, Actual: 8640/11"""
