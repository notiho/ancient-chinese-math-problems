"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the leg (gu) and the hypotenuse (xian) is 1337 1/20 (or 1337 + 1/20), and the hypotenuse is 1 1/10 (or 1 + 1/10) more than the other leg (gu). 
Question: how long is the leg (gu)?

Answer: *a*.
"""

from fractions import Fraction

# Given values
product = Fraction(1337, 1) + Fraction(1, 20)  # The product of gu and xian
difference = Fraction(1, 1) + Fraction(1, 10)  # The difference between xian and gu

# Let gu = x, and xian = x + difference
# The product of gu and xian is given as:
# x * (x + difference) = product
# Solve for x (gu)

# Expand the equation: x^2 + difference * x = product
# Rearrange: x^2 + difference * x - product = 0

# Coefficients of the quadratic equation
a_coeff = 1
b_coeff = difference
c_coeff = -product

# Solve using the quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / 2a
# Since gu (x) must be positive, we only take the positive root.

# Calculate the discriminant
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff

# Calculate the positive root
gu = (-b_coeff + discriminant**0.5) / (2 * a_coeff)

# Final answer
a = gu
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 36.01983046173444"""
