"""
今有箕田一頭廣八十六步一頭廣四十步從九十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a trapezoidal field (箕田) with one side of width 86 bu, the other side of width 40 bu, and a length of 90 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Define the dimensions of the trapezoidal field
廣頭1 = 86  # One side of the width in bu
廣頭2 = 40  # The other side of the width in bu
從 = 90      # Length in bu

# Calculate the area in bu² using the formula for the area of a trapezoid
area_in_bu2 = Fraction((廣頭1 + 廣頭2) * 從, 2)

# Convert the area into mu and remaining bu
# 1 mu = 240 bu²
a = area_in_bu2 // 240  # Whole mu
b = area_in_bu2 % 240   # Remaining bu²

a, b  # Output the result as (a mu, b bu)
"""
"""
