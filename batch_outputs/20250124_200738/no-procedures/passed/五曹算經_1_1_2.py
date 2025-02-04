"""
今有方田廣從各六十八步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with both width and length of 68 bu.
Question: how large is the field?

Answer: it is *a* mu and an additional *b* bu.
"""

from fractions import Fraction

# 方田廣從各六十八步
廣 = 68
從 = 68

# Calculate the total area in bu²
total_area_bu = 廣 * 從

# Convert bu² to mu (1 mu = 240 bu²)
a = total_area_bu // 240  # Integer part (whole mu)
b = total_area_bu % 240   # Remainder (additional bu²)

# Output the result
a, b#----- content ends here -----

"""
"""
