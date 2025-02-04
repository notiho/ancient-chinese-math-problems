"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is an irregular (trapezoidal) field. One end has a width of 30 bu, the other end has a width of 42 bu, and the length (height) is 64 bu.
Question: how large is the field?

Answer: it makes *a* mu.
"""

from fractions import Fraction

# 一頭廣三十步
廣1 = 30

# 一頭廣四十二步
廣2 = 42

# 正從六十四步
從 = 64

# Calculate the area in square bu (trapezoid area formula: (base1 + base2) * height / 2)
area_in_bu = (廣1 + 廣2) * 從 / 2

# Convert the area into mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
