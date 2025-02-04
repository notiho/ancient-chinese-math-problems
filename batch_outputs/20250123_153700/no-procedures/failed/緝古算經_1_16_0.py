"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
答曰： a 。
"""

"""
Suppose there is a right triangle where the product of the legs (ju and xian) is 1337 1/20. The hypotenuse (xian) is longer than the base (gu) by 1 1/10.
Question: what is the length of the base (gu)?

Answer: *a*.
"""

from fractions import Fraction

# Given values
product_of_ju_and_xian = Fraction(1337, 1) + Fraction(1, 20)  # 1337 1/20
difference_between_xian_and_gu = Fraction(1, 1) + Fraction(1, 10)  # 1 1/10

# Let gu = x, xian = x + difference_between_xian_and_gu
# The product of gu and xian is given as:
# gu * xian = product_of_ju_and_xian
# x * (x + difference_between_xian_and_gu) = product_of_ju_and_xian
# x^2 + difference_between_xian_and_gu * x - product_of_ju_and_xian = 0

# Coefficients of the quadratic equation
a_coeff = 1
b_coeff = difference_between_xian_and_gu
c_coeff = -product_of_ju_and_xian

# Solve the quadratic equation using the quadratic formula:
# x = (-b ± sqrt(b^2 - 4ac)) / 2a

# Calculate the discriminant
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff

# Calculate the two possible solutions for gu
gu1 = (-b_coeff + discriminant**0.5) / (2 * a_coeff)
gu2 = (-b_coeff - discriminant**0.5) / (2 * a_coeff)

# Since gu must be positive, we choose the positive solution
a = gu1 if gu1 > 0 else gu2

a
"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 36.01983046173444"""
