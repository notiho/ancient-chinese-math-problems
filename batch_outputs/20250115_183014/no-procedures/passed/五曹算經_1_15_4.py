"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a field shaped like a cow's horn (a trapezoid) with a length of 50 bu and a width at the mouth of 20 bu.
Question: What is the area of the field?

Answer: The area is *a* mu and *b* bu.
"""

from fractions import Fraction

# Given dimensions
length = 50  # bu
mouth_width = 20  # bu
narrow_width = 0  # bu (since the other end of the cow horn is assumed to taper to a point)

# Formula for the area of a trapezoid: (width1 + width2) * length / 2
area_in_bu = (mouth_width + narrow_width) * length / 2

# Convert the area into mu and bu
# 1 mu = 240 bu
a = area_in_bu // 240  # Whole mu
b = area_in_bu % 240  # Remaining bu

# Output the results
a = Fraction(a)
b = Fraction(b)
"""
"""
