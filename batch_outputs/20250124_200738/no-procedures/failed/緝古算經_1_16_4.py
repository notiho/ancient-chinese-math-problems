"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the legs (ju and xian) is 1337 and 1/20 (1337 + 1/20). The hypotenuse (xian) is longer than the base (gu) by 1 and 1/10 (1 + 1/10). 
Question: how long is the base (gu)?

Answer: *a*.
"""

from fractions import Fraction

# Given values
ju_xian_product = Fraction(1337, 1) + Fraction(1, 20)  # The product of the legs
xian_minus_gu = Fraction(1, 1) + Fraction(1, 10)       # Difference between hypotenuse and base

# Let gu = x, then xian = x + xian_minus_gu
# From the problem: ju * xian = ju_xian_product
# Substituting xian = x + xian_minus_gu:
# ju * (x + xian_minus_gu) = ju_xian_product
# ju = ju_xian_product / (x + xian_minus_gu)

# Solve for gu (x):
# x * (x + xian_minus_gu) = ju_xian_product
# x^2 + xian_minus_gu * x - ju_xian_product = 0

# Coefficients of the quadratic equation
a_coeff = 1
b_coeff = xian_minus_gu
c_coeff = -ju_xian_product

# Solve the quadratic equation using the quadratic formula:
# x = (-b ± sqrt(b^2 - 4ac)) / 2a

# Calculate discriminant
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff

# Calculate the two possible solutions for x (gu)
gu1 = (-b_coeff + discriminant**0.5) / (2 * a_coeff)
gu2 = (-b_coeff - discriminant**0.5) / (2 * a_coeff)

# Since gu must be positive, we choose the positive solution
a = gu1 if gu1 > 0 else gu2

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 36.01983046173444"""
