"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
答曰： a畝
"""

#----- content starts here -----
"""
Suppose there is a field shaped like a trapezoid. One of its parallel sides (widths) is 25 bu, and the other is 35 bu. The length (height) of the field is 48 bu.
Question: how large is the field in mu?

Answer: it is *a* mu.
"""

from fractions import Fraction

# Dimensions of the field
length = 48  # Length (height) in bu
width1 = 25  # One width in bu
width2 = 35  # Other width in bu

# Calculate the area in square bu (trapezoid area formula: (width1 + width2) * length / 2)
area_in_bu = (width1 + width2) * length // 2

# Convert the area from square bu to mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)

# Output the result
a#----- content ends here -----

"""
"""
