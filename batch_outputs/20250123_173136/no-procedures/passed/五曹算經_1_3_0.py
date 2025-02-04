"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a wedge-shaped field (圭田) where one end has a length of 30 bu, the other end has a length of 0 bu, and the width is 24 bu.
Question: how large is the field?

Answer: it is *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
從一頭 = 30  # Length of one end in bu
從二頭 = 0   # Length of the other end in bu
廣 = 24      # Width in bu

# Calculate the area of the wedge-shaped field
# Area = (average length) * width
area_in_bu = Fraction((從一頭 + 從二頭), 2) * 廣

# Convert the area into mu and remaining bu
# 1 mu = 240 bu
a = area_in_bu // 240  # Whole mu
b = area_in_bu % 240   # Remaining bu

a, b  # Output the result as (a mu, b bu)
"""
"""
