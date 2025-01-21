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

# Known values
冪 = 726  # Product of gu and xian
句 = Fraction(77, 10)  # The length of ju (7 and 7/10)

# Using the Pythagorean theorem: gu^2 + ju^2 = xian^2
# Also, gu * xian = 冪
# From gu * xian = 冪, we can express xian as 冪 / gu.
# Substituting into the Pythagorean theorem:
# gu^2 + ju^2 = (冪 / gu)^2
# Multiply through by gu^2 to eliminate the fraction:
# gu^4 - (ju^2) * gu^2 - 冪^2 = 0

# Let us solve for gu step by step.

# Step 1: Calculate ju^2
句平方 = 句**2

# Step 2: Use the quadratic equation to solve for gu^2
# gu^4 - (ju^2) * gu^2 - 冪^2 = 0
# Let x = gu^2, then the equation becomes:
# x^2 - (ju^2) * x - 冪^2 = 0

# Coefficients of the quadratic equation
A = 1
B = -句平方
C = -冪**2

# Solve for x (gu^2) using the quadratic formula: x = (-B ± sqrt(B^2 - 4AC)) / 2A
# Since gu^2 must be positive, we take the positive root.

# Calculate discriminant
discriminant = B**2 - 4 * A * C

# Positive root
gu平方 = Fraction(-B + discriminant**0.5, 2 * A)

# Step 3: Take the square root of gu^2 to find gu
a = gu平方**0.5

# Final result
a
"""
Code error: both arguments should be Rational instances"""
