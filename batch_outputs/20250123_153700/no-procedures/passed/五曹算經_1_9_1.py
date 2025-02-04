"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
答曰： a畝
"""

"""
Suppose there is a field shaped like a trapezoid. One of the parallel sides (widths) is 25 bu, and the other is 35 bu. The length (height) between the two parallel sides is 48 bu.
Question: how large is the area of the field?

Answer: *a* mu.
"""

from fractions import Fraction

# Dimensions of the field
length = 48  # 從 (length) in bu
width1 = 25  # 一頭廣 (one width) in bu
width2 = 35  # 另一頭廣 (the other width) in bu

# Calculate the area in square bu
area_in_bu = Fraction((width1 + width2) * length, 2)

# Convert the area from square bu to mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)

# Output the result
a
"""
"""
