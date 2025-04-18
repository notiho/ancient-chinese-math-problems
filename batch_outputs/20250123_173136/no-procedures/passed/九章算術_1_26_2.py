"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is an irregular (trapezoidal) field. One side has a width of 30 bu, the other side has a width of 42 bu, and the length is 64 bu.
Question: how large is the area of the field?

Answer: it makes *a* mu.
"""

from fractions import Fraction

# 一頭廣三十步
廣1 = 30

# 一頭廣四十二步
廣2 = 42

# 正從六十四步
從 = 64

# Calculate the area in square bu using the formula for the area of a trapezoid: (width1 + width2) / 2 * length
area_in_bu = Fraction((廣1 + 廣2), 2) * 從

# Convert the area into mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)

# Output the result
a
"""
"""
