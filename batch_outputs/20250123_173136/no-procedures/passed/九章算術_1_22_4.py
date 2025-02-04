"""
又有田廣七步、四分步之三，從十五步、九分步之五。問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a field with a width of 7 bu and 3/4 of a bu, and a length of 15 bu and 5/9 of a bu.
Question: how large is the area of the field?

Answer: *a* bu².
"""

from fractions import Fraction

# 廣七步、四分步之三
廣 = 7 + Fraction(3, 4)

# 從十五步、九分步之五
從 = 15 + Fraction(5, 9)

# Calculate the area by multiplying width and length
a = 廣 * 從

a  # The area in bu²
"""
"""
