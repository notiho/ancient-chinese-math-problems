"""
今有田廣一步半、三分步之一。求田一畝，問︰從幾何？
術曰：下有三分，以一為六，半為三，三分之一為二，并之得一十一為法。置田二百四十步，亦以一為六乘之，為實。實如法得從步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
田廣 = Fraction(1, 2) + Fraction(1, 3)  # 一步半、三分步之一

# Conversion factor
一畝 = 240  # 240 steps in one 畝
一為六 = 6  # Each step is multiplied by 6 to convert

# Calculate 法
法 = 田廣 * 一為六  # Combine the fractions and multiply by 6

# Calculate 實
實 = 一畝 * 一為六  # Multiply 240 steps by 6

# Calculate 從步
a = 實 / 法  # Divide 實 by 法 to find the answer in steps

# The answer is stored in variable 'a'
a


"""


This code computes the value of `a` in steps using the given problem and the ancient Chinese method. The result will be a `Fraction` representing the number of steps.
"""


"""
Variable 'a' has wrong value. Expected: 1440/11, Actual: 288"""
