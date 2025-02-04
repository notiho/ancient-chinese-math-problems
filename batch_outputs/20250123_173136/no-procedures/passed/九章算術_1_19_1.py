"""
又有田廣九分步之七，從十一分步之九。問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a field with a width of 7/9 bu and a length of 9/11 bu.
Question: how large is the field?

Answer: *a* bu.
"""

from fractions import Fraction

# 廣九分步之七
廣 = Fraction(7, 9)

# 從十一分步之九
從 = Fraction(9, 11)

# Multiply width and length to get the area
a = 廣 * 從

# Output the result
a
"""
"""
