"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
答曰： a畝
"""

"""
Suppose there is a trapezoidal field. One parallel side (shorter width) is 25 bu, the other parallel side (longer width) is 35 bu, and the length (height) between them is 48 bu.
Question: how large is the field?

Answer: *a* mu.
"""

from fractions import Fraction

# Dimensions of the field
shorter_width = 25  # in bu
longer_width = 35   # in bu
length = 48         # in bu

# Area of the trapezoid in square bu
area_in_bu = Fraction((shorter_width + longer_width) * length, 2)

# Convert square bu to mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)

# Result
a
"""
"""
