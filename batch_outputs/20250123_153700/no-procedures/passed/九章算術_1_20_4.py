"""
又有田廣五分步之四，從九分步之五，問：為田幾何？
荅曰： a步 。
"""

"""
Suppose there is a field with a width of 4/5 bu and a length of 5/9 bu.
Question: how large is the field?

Answer: *a* bu.
"""

from fractions import Fraction

# 廣五分步之四
廣 = Fraction(4, 5)

# 從九分步之五
從 = Fraction(5, 9)

# Calculate the area of the field
a = 廣 * 從

# Output the result
a
"""
"""
