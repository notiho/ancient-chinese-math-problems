"""
今有方田，廣從各五十六步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a square field, with both its width and length being 56 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
廣 = 56  # Width in bu
從 = 56  # Length in bu

# Calculate total area in bu²
田積 = 廣 * 從

# Convert to mu (1 mu = 240 bu²)
a = 田積 // 240  # Whole mu
b = 田積 % 240   # Remaining bu²

# Output
a, b
"""
"""
