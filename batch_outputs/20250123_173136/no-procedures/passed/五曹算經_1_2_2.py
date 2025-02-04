"""
今有直田廣八十步從一百九十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a rectangular field with a width of 80 bu and a length of 190 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 廣八十步
廣 = 80

# 從一百九十步
從 = 190

# Calculate the total area in square bu
總面積 = 廣 * 從

# Convert the total area into mu and bu
# 1 mu = 240 square bu
a = 總面積 // 240  # Whole mu
b = 總面積 % 240   # Remaining bu

a = Fraction(a)
b = Fraction(b)

a, b
"""
"""
