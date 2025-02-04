"""
今有句五步，股十二步。問︰句中容方幾何？
術曰：并句、股為法，句股相乘為實，實如法而一，得方一步。
荅曰：方 a步 。
"""

"""
This problem is a classic example of the Pythagorean theorem in ancient Chinese mathematics. The problem involves finding the hypotenuse (方, "a") of a right triangle given the lengths of the other two sides (句 and 股). Here's the Python code to compute the solution:


"""


from fractions import Fraction

# Given values
句 = Fraction(5)  # 5 steps
股 = Fraction(12)  # 12 steps

# Compute the hypotenuse (方, "a")
a = (句**2 + 股**2)**Fraction(1, 2)  # Pythagorean theorem

# The result is stored in variable "a"


"""


The value of `a` will be the hypotenuse in steps.
"""


"""
Variable 'a' has wrong value. Expected: 60/17, Actual: 13.0"""
