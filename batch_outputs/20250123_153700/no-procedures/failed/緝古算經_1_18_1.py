"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
答曰：股 a 。
"""

"""
Suppose there is a right triangle where the product of the leg (gu) and the hypotenuse (xian) is 726, and the other leg (ju) is 7 and 7/10 (7.7 in decimal form).
Question: how long is the other leg (gu)?

Answer: the other leg (gu) is *a*.
"""

from fractions import Fraction

# Given values
冪 = 726  # Product of gu and xian
句 = Fraction(77, 10)  # The length of ju (7 and 7/10)

# Using the Pythagorean theorem: gu^2 + ju^2 = xian^2
# Also given: gu * xian = 726
# From gu * xian = 726, we can express xian as xian = 726 / gu
# Substituting into the Pythagorean theorem:
# gu^2 + ju^2 = (726 / gu)^2
# Multiply through by gu^2 to eliminate the fraction:
# gu^4 + ju^2 * gu^2 = 726^2
# Solve for gu.

# Step 1: Calculate ju^2
句平方 = 句**2

# Step 2: Substitute into the equation
# gu^4 + (ju^2 * gu^2) = 726^2
# Let gu^2 = x, then the equation becomes:
# x^2 + (ju^2 * x) - 726^2 = 0
# This is a quadratic equation in terms of x.

# Coefficients of the quadratic equation
a = 1
b = 句平方
c = -726**2

# Solve for gu^2 using the quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / 2a
discriminant = b**2 - 4 * a * c
gu平方 = Fraction(-b + discriminant**0.5, 2 * a)  # Taking the positive root since length must be positive

# Step 3: Calculate gu
gu = gu平方**0.5

# Final answer
a = gu
a
"""
Code error: both arguments should be Rational instances"""
