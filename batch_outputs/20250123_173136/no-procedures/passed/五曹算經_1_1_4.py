"""
今有方田廣從各六十八步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a square field with both width and length of 68 bu.
Question: how large is the field?

Answer: it makes *a* mu and an additional *b* bu.
"""

from fractions import Fraction

# 方田廣從各六十八步
廣 = 68
從 = 68

# Calculate the total area in bu²
total_area_bu2 = 廣 * 從

# Convert to mu (1 mu = 240 bu²)
a = total_area_bu2 // 240  # Integer part (mu)
b = total_area_bu2 % 240   # Remainder (bu²)

a = int(a)
b = int(b)
"""
"""
