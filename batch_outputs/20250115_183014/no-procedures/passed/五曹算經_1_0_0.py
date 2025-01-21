"""
今有方田，廣從各五十六步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a square field with both the width and length being 56 bu.
Question: how large is the field?

Answer: it is *a* mu and *b* bu.
"""

from fractions import Fraction

# The width and length of the square field
廣 = 56  # bu
從 = 56  # bu

# Calculate the total area in bu²
total_area_bu2 = 廣 * 從

# Convert bu² to mu (1 mu = 240 bu²)
a = total_area_bu2 // 240  # Whole mu
b = total_area_bu2 % 240   # Remaining bu²

# Output the result
a, b  # a is the number of mu, b is the remaining bu²
"""
"""
