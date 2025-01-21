"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a trapezoidal field (箕田) where one side has a width of 86 bu, the other side has a width of 40 bu, and the length is 90 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 一頭廣八十六步
head1_width = 86

# 一頭廣四十步
head2_width = 40

# 從九十步
length = 90

# Calculate the area in bu² using the formula for the area of a trapezoid: (a + b) * h / 2
area_in_bu2 = (head1_width + head2_width) * length // 2

# Convert the area into mu and remaining bu
# 1 mu = 240 bu²
a = area_in_bu2 // 240  # Full mu
b = area_in_bu2 % 240   # Remaining bu

a, b  # Output the result as a mu and b bu
"""
"""
