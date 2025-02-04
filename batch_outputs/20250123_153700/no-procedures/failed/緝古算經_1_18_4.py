"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
答曰：股 a 。
"""

"""
Suppose the product of the leg (gu) and hypotenuse (xian) of a right triangle is 726, and the other leg (ju) is 7 and 7/10 (7.7).
Question: what is the length of the other leg (gu)?

Answer: the leg (gu) is *a*.
"""

from fractions import Fraction

# Given values
冪 = 726  # Product of gu and xian
句 = Fraction(77, 10)  # Length of ju (7 and 7/10)

# Using the Pythagorean theorem: gu^2 + ju^2 = xian^2
# Also given: gu * xian = 冪
# From gu * xian = 冪, we can express xian as 冪 / gu.
# Substituting into the Pythagorean theorem:
# gu^2 + ju^2 = (冪 / gu)^2
# Multiply through by gu^2 to eliminate the fraction:
# gu^4 - (ju^2) * gu^2 - 冪^2 = 0
# Solve for gu.

# Step 1: Calculate ju^2
句平方 = 句**2

# Step 2: Use the quadratic equation to solve for gu^2
# Let x = gu^2, then the equation becomes:
# x^2 - 句平方 * x - 冪^2 = 0
# Solve using the quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / 2a
a = 1
b = -句平方
c = -冪**2

# Discriminant
discriminant = b**2 - 4 * a * c

# gu^2 is the positive root
股平方 = (-b + discriminant**0.5) / (2 * a)

# Step 3: Take the square root to find gu
a = 股平方**0.5

# Final result
a
"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 27.5"""
