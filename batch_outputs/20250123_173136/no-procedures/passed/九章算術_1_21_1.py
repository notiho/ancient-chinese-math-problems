"""
今有田廣三步、三分步之一，從五步、五分步之二。問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a field with a width of 3 bu and 1/3 bu, and a length of 5 bu and 2/5 bu.
Question: how large is the field?

Answer: it makes *a* bu².
"""

from fractions import Fraction

# 廣三步、三分步之一
廣 = 3 + Fraction(1, 3)

# 從五步、五分步之二
從 = 5 + Fraction(2, 5)

# Calculate the area
a = 廣 * 從

# Output the result
a
"""
"""
