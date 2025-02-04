"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a field shaped like a cow's horn (a trapezoid) with a length of 50 bu and a width at the mouth of 20 bu.
Question: how large is the field?

Answer: *a* mu and an additional *b* bu.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Given dimensions
length = 50  # 從 (length) in bu
mouth_width = 20  # 口廣 (width at the mouth) in bu

# The formula for the area of a trapezoid is:
# Area = (length * mouth_width) / 2
area_in_bu = Fraction(length * mouth_width, 2)

# Convert the area into mu and remaining bu
# 1 mu = 240 bu
a = area_in_bu // 240  # Whole mu
b = area_in_bu % 240  # Remaining bu

# Output the results
a, b  # a is the number of mu, b is the remaining bu#----- content ends here -----

"""
"""
