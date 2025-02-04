"""
今有圭田從三十步一頭廣二十四步一頭無步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a wedge-shaped field (圭田) with one side of the length being 30 bu, the other side of the length being 0 bu, and the width being 24 bu.
Question: how large is the field?

Answer: it is *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
長_一頭 = 30  # Length of one side in bu
長_另一頭 = 0  # Length of the other side in bu
廣 = 24  # Width in bu

# Calculate the area of the wedge-shaped field
# Area = (average length) * width
田積_in_bu = Fraction((長_一頭 + 長_另一頭), 2) * 廣

# Convert the area into mu and remaining bu
# 1 mu = 240 bu
a = 田積_in_bu // 240  # Whole mu
b = 田積_in_bu % 240  # Remaining bu

a, b  # Output the result as (a mu, b bu)
"""
"""
