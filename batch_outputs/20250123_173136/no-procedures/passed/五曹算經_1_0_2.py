"""
今有方田，廣從各五十六步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a square field, with both the width and length being 56 bu.
Question: how large is the field?

Answer: it is *a* mu and an additional *b* bu.
"""

from fractions import Fraction

# 廣從各五十六步
廣 = 56
從 = 56

# Calculate the total area in square bu
total_area_bu = 廣 * 從

# Convert to mu (1 mu = 240 square bu)
a = total_area_bu // 240  # Whole mu
b = total_area_bu % 240   # Remaining bu

a, b  # Output the result as (a mu, b bu)
"""
"""
