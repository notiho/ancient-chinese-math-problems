"""
今有田廣七分步之四，從五分步之三。問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a field with a width of 7/4 bu and a length of 5/3 bu.
Question: how large is the field?

Answer: *a* bu.
"""

from fractions import Fraction

# 廣七分步之四
廣 = Fraction(7, 4)

# 從五分步之三
從 = Fraction(5, 3)

# Multiply width and length to get the area
a = 廣 * 從

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 12/35, Actual: 35/12"""
