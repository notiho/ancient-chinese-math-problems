"""
假令有句弦相乘冪一千三百三十七二十分之一，弦多股一、十分之一。問：股多少？
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the legs (ju and xian) is 1337 and 1/20. The hypotenuse (xian) exceeds the base (gu) by 1 and 1/10.
Question: what is the length of the base (gu)?

Answer: *a*.
"""

from fractions import Fraction

# Given values
product_of_legs = Fraction(1337, 1) + Fraction(1, 20)  # 1337 + 1/20
difference = Fraction(1, 1) + Fraction(1, 10)  # 1 + 1/10

# Let gu = x (base) and xian = x + difference
# The product of gu and xian is given as:
# gu * xian = product_of_legs
# x * (x + difference) = product_of_legs
# x^2 + difference * x - product_of_legs = 0

# Coefficients of the quadratic equation
a_coeff = 1
b_coeff = difference
c_coeff = -product_of_legs

# Solve the quadratic equation using the quadratic formula:
# x = (-b ± sqrt(b^2 - 4ac)) / 2a

# Calculate discriminant
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff

# Since the base (gu) must be positive, we take the positive root
gu = (-b_coeff + discriminant**0.5) / (2 * a_coeff)

# Final answer
a = gu
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 462/5, Actual: 36.01983046173444"""
