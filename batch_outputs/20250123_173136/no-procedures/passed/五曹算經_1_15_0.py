"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a field shaped like an ox horn (a trapezoid) with a length of 50 bu and a width at the wider end of 20 bu, while the narrower end is 0 bu.
Question: how large is the area of the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Given dimensions
length = 50  # bu (從)
wide_end = 20  # bu (口廣)
narrow_end = 0  # bu (narrow end width)

# Area of a trapezoid: (wide_end + narrow_end) * length / 2
area_in_bu = (wide_end + narrow_end) * length / 2

# Convert bu^2 to mu (1 mu = 240 bu^2)
a = int(area_in_bu // 240)  # Whole mu
b = area_in_bu % 240  # Remaining bu

# Output results
a, b  # a mu and b bu
"""
"""
