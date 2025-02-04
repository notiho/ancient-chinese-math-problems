"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (箕田) where one side is 86 bu wide, the other side is 40 bu wide, and the length is 90 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 一頭廣八十六步
廣1 = 86

# 一頭廣四十步
廣2 = 40

# 從九十步
從 = 90

# Calculate the area in bu² using the formula for the area of a trapezoid: (廣1 + 廣2) * 從 / 2
area_in_bu2 = (廣1 + 廣2) * 從 // 2

# Convert the area into mu and bu (1 mu = 240 bu²)
a = area_in_bu2 // 240  # Whole mu
b = area_in_bu2 % 240   # Remaining bu²

# Output the result
a, b#----- content ends here -----

"""
"""
