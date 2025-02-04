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

# 直田廣八十步
廣 = 80

# 從一百九十步
從 = 190

# Calculate the total area in square bu
total_area_bu = 廣 * 從

# Convert the area into mu (1 mu = 240 square bu)
a = total_area_bu // 240  # Integer part (whole mu)
b = total_area_bu % 240   # Remainder (remaining bu)

# Output the result
a, b  # a is the number of mu, b is the remaining bu
"""
"""
