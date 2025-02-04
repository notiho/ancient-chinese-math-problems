"""
假令有股弦相乘冪七百二十六，句七、十分之七。問：股多少？
答曰：股 a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the leg (gu) and the hypotenuse (xian) is 726, and the other leg (ju) is 7 and 7/10 (7.7 in decimal form).
Question: how long is the other leg (gu)?

Answer: the leg (gu) is *a*.
"""

from fractions import Fraction

# Given values
冪 = 726  # The product of gu and xian
句 = Fraction(77, 10)  # The length of ju (7 and 7/10)

# Using the Pythagorean theorem: gu^2 + ju^2 = xian^2
# Also given: gu * xian = 冪
# From gu * xian = 冪, we can express xian as 冪 / gu
# Substitute xian into the Pythagorean theorem:
# gu^2 + ju^2 = (冪 / gu)^2
# Multiply through by gu^2 to eliminate the fraction:
# gu^4 + ju^2 * gu^2 = 冪^2
# Solve for gu^2:
# gu^4 + (句^2) * gu^2 - 冪^2 = 0

# Step 1: Calculate ju^2 and 冪^2
句平方 = 句**2
冪平方 = 冪**2

# Step 2: Solve the quadratic equation for gu^2
# Let x = gu^2, then the equation becomes:
# x^2 + (句平方) * x - 冪平方 = 0
# Solve using the quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / 2a
# Here, a = 1, b = 句平方, c = -冪平方

a = 1
b = 句平方
c = -冪平方

# Discriminant
discriminant = b**2 - 4 * a * c

# gu^2 (taking the positive root since length must be positive)
股平方 = (-b + discriminant**0.5) / (2 * a)

# Step 3: Calculate gu by taking the square root of 股平方
a = 股平方**0.5

# Final result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 132/5, Actual: 26.400000000000002"""
