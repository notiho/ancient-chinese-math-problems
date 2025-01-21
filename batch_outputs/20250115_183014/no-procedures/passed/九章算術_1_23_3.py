"""
又有田廣十八步、七分步之五，從二十三步、十一分步之六。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is a field with a width of 18 bu and 5/7 of a bu, and a length of 23 bu and 6/11 of a bu.
Question: how large is the field?

Answer: *a* mu.
"""

from fractions import Fraction

# 廣 (width): 18步 + 5/7步
廣 = 18 + Fraction(5, 7)

# 從 (length): 23步 + 6/11步
從 = 23 + Fraction(6, 11)

# 面積 (area) in square bu
面積 = 廣 * 從

# Convert square bu to mu (1 mu = 240 square bu)
a = 面積 / 240

# Output the result
a
"""
"""
