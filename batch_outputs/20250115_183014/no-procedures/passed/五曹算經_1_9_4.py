"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
答曰： a畝
"""

"""
Suppose there is a field shaped like a trapezoid. One side of the length is 48 bu, one side of the width is 25 bu, and the other side of the width is 35 bu.
Question: how large is the field?

Answer: *a* mu.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Given dimensions
從 = 48  # Length (bu)
廣1 = 25  # One width (bu)
廣2 = 35  # Other width (bu)

# Calculate the area of the trapezoid in square bu
area_in_bu = Fraction(從 * (廣1 + 廣2), 2)

# Convert the area into mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)

# Output the result
a
"""
"""
