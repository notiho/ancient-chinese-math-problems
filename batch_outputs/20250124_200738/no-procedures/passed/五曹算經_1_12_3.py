"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (箕田) where one side is 86 bu wide, the other side is 40 bu wide, and the length (height) is 90 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# One side of the trapezoid
廣1 = 86

# The other side of the trapezoid
廣2 = 40

# The length (height)
從 = 90

# The area of the trapezoid is calculated as:
# Area = (廣1 + 廣2) * 從 / 2
area_in_bu = (廣1 + 廣2) * 從 // 2

# Convert the area into mu and remaining bu:
# 1 mu = 240 bu
a = area_in_bu // 240  # Whole mu
b = area_in_bu % 240   # Remaining bu

a, b  # Output the result as (a mu, b bu)#----- content ends here -----

"""
"""
