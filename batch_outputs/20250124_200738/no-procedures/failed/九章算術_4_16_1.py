"""
今有積一千五百一十八步、四分步之三。問︰為圓周幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is an area of 1518 and 3/4 bu² (square bu). The area is circular.
Question: what is the circumference of the circle?

Answer: the circumference is *a* bu.
"""

from fractions import Fraction

# Given area
area = 1518 + Fraction(3, 4)

# Formula for the area of a circle: A = (C / 4)^2 * π
# Rearranging to solve for circumference (C):
# C = 4 * sqrt(A / π)

# Using π ≈ 3 for ancient Chinese calculations
pi = 3

# Solve for circumference
circumference = 4 * (area / pi) ** Fraction(1, 2)

# Result
a = circumference
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 135, Actual: 90.0"""
