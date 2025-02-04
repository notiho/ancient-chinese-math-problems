"""
又有田廣十八步、七分步之五，從二十三步、十一分步之六。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a field with a width of 18 bu and 5/7 of a bu, and a length of 23 bu and 6/11 of a bu.
Question: how large of a field does it make?

The answer says: *a* mu.
"""

from fractions import Fraction

# 廣十八步、七分步之五
廣 = 18 + Fraction(5, 7)

# 從二十三步、十一分步之六
從 = 23 + Fraction(6, 11)

# Multiply width and length to get the area in square bu
area_in_bu = 廣 * 從

# Convert square bu to mu (1 mu = 240 square bu)
a = area_in_bu / 240

# Output the result
a
"""
"""
