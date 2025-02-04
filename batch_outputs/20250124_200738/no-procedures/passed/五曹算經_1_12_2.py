"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (箕田) with one end 86 bu wide, the other end 40 bu wide, and a length of 90 bu.
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

# Calculate the area in bu² using the formula for the area of a trapezoid: (廣1 + 廣2) / 2 * 從
area_in_bu2 = Fraction((廣1 + 廣2), 2) * 從

# Convert the area into mu and remaining bu
# 1 畝 = 240 bu²
a = area_in_bu2 // 240  # Integer part (mu)
b = area_in_bu2 % 240   # Remainder (bu)

# Output the results
a, b  # a is in mu, b is in bu#----- content ends here -----

"""
"""
