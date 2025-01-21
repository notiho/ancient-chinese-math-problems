"""
又有田廣七步、四分步之三，從十五步、九分步之五。問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a field with a width of 7 bu and 3/4 of a bu, and a length of 15 bu and 5/9 of a bu.
Question: how large is the field?

The answer says: *a* bu².
"""

from fractions import Fraction

# 廣七步、四分步之三
廣 = 7 + Fraction(3, 4)

# 從十五步、九分步之五
從 = 15 + Fraction(5, 9)

# Multiply width and length to get the area
a = 廣 * 從

a  # The area in bu²
"""
"""
