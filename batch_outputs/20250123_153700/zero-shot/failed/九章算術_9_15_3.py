"""
今有句八步，股十五步。問︰句中容圓，徑幾何？
術曰：八步為句，十五步為股，為之求弦。三位并之為法，以句乘股，倍之為實。實如法得徑一步。
荅曰： a步 。
"""

"""
This problem is a classic example of the Pythagorean theorem. The problem involves finding the hypotenuse (弦) of a right triangle where the two legs (句 and 股) are given. The hypotenuse corresponds to the diameter of the circle (徑). Here's the Python code to compute the value of `a`:


"""


from fractions import Fraction

# Given values
句 = Fraction(8)  # 8 steps
股 = Fraction(15)  # 15 steps

# Compute the hypotenuse (弦), which is the diameter (徑)
a = (句**2 + 股**2)**Fraction(1, 2)

# The answer is stored in variable 'a'


"""
 

The value of `a` represents the diameter of the circle in steps.
"""


"""
Variable 'a' has wrong value. Expected: 6, Actual: 17.0"""
