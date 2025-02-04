"""
假令有股十六二分之一，句弦相乘冪一百六十四二十五分之十四。問：句多少？
答曰：句 a 。
"""

"""
Suppose there is a right triangle where the leg (gu) is 16 1/2 (16.5), and the product of the other leg (ju) and the hypotenuse (xian) is 164 14/25 (164.56).
Question: what is the length of the other leg (ju)?

Answer: the length of the other leg is *a*.
"""

from fractions import Fraction

# 股 (gu) = 16 1/2
gu = Fraction(33, 2)

# 句弦相乘冪 = 164 14/25
ju_xian_product = Fraction(164 * 25 + 14, 25)

# Using the relationship: ju * xian = ju_xian_product
# And the Pythagorean theorem: gu^2 + ju^2 = xian^2
# We solve for ju.

# Step 1: Express xian in terms of ju and gu using the product relationship:
# xian = ju_xian_product / ju

# Step 2: Substitute xian into the Pythagorean theorem:
# gu^2 + ju^2 = (ju_xian_product / ju)^2

# Step 3: Multiply through by ju^2 to eliminate the denominator:
# gu^2 * ju^2 + ju^4 = ju_xian_product^2

# Step 4: Rearrange into a standard quadratic form in terms of ju^2:
# ju^4 + gu^2 * ju^2 - ju_xian_product^2 = 0

# Let z = ju^2, then solve the quadratic equation:
# z^2 + gu^2 * z - ju_xian_product^2 = 0

# Coefficients of the quadratic equation:
gu_squared = gu**2
ju_xian_product_squared = ju_xian_product**2

# Solve for z (ju^2) using the quadratic formula:
# z = (-b ± sqrt(b^2 - 4ac)) / 2a
# Here, a = 1, b = gu^2, c = -ju_xian_product^2

a = 1
b = gu_squared
c = -ju_xian_product_squared

discriminant = b**2 - 4 * a * c

# Only the positive root is meaningful:
z = (-b + discriminant**0.5) / (2 * a)

# ju = sqrt(z)
ju = z**0.5

# Final answer:
a = ju
a
"""
Variable 'a' has wrong value. Expected: 44/5, Actual: 8.8"""
