"""
今有直田廣八十步從一百九十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
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

# Calculate total area in square bu
total_area_bu = 廣 * 從

# Convert total area into mu (1 mu = 240 square bu)
a = total_area_bu // 240  # Whole mu
b = total_area_bu % 240   # Remaining bu

# Output: a mu and b bu
a, b#----- content ends here -----

"""
"""
