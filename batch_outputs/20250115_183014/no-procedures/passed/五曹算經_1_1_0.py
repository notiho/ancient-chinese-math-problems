"""
今有方田廣從各六十八步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a square field with both width and length of 68 bu.
Question: how large is the field?

Answer: It is *a* mu and an additional *b* bu.
"""

from fractions import Fraction

# 方田廣從各六十八步
邊長 = 68

# Calculate the total area in bu^2
總面積 = 邊長 * 邊長

# Convert to mu (1 mu = 240 bu^2)
a = 總面積 // 240  # Integer part in mu
b = 總面積 % 240   # Remainder in bu^2

a, b  # Output the result as (a mu, b bu)
"""
"""
