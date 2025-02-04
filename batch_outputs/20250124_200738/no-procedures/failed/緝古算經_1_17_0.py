"""
假令有股弦相乘冪四千七百三十九五分之三，句少於弦五十四五分之二。問：股多少？
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle where the product of the leg (gu) and the hypotenuse (xian) is 4739 and 3/5 (4739 + 3/5). 
The other leg (ju) is shorter than the hypotenuse by 54 and 2/5 (54 + 2/5).
Question: how long is the other leg (gu)?

Answer: *a*.
"""

from fractions import Fraction

# Given values
冪 = Fraction(4739, 1) + Fraction(3, 5)  # 股弦相乘冪
差 = Fraction(54, 1) + Fraction(2, 5)    # 句少於弦

# Let 股 = x, 弦 = y
# From the problem:
# x * y = 冪
# y - 句 = 差 -> y = x + 差

# Substitute y = x + 差 into x * y = 冪
# x * (x + 差) = 冪
# x^2 + 差 * x - 冪 = 0

# Coefficients of the quadratic equation
a_coeff = 1
b_coeff = 差
c_coeff = -冪

# Solve the quadratic equation using the quadratic formula: x = (-b ± √(b^2 - 4ac)) / 2a
discriminant = b_coeff**2 - 4 * a_coeff * c_coeff

# Since x must be positive, we take the positive root
股 = (-b_coeff + discriminant**0.5) / (2 * a_coeff)

# Final answer
a = 股
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 68, Actual: 46.82323959406261"""
