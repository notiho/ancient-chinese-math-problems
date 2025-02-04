"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a waist-drum-shaped field (trapezoidal field) with a length of 82 bu.
The two ends are each 30 bu wide, and the middle is 12 bu wide.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
length = 82  # 從 (length)
end_width = 30  # 两頭各廣 (width at both ends)
middle_width = 12  # 中央廣 (width in the middle)

# Calculate the average width using the formula for a waist-drum-shaped field
average_width = Fraction(end_width + middle_width, 2)

# Calculate the total area in bu²
area_in_bu = length * average_width

# Convert the area into mu and remaining bu
a = area_in_bu // 240  # 1 mu = 240 bu²
b = area_in_bu % 240  # Remaining bu²

# Output the results
a, b  # a is in mu, b is in bu²#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 8, Actual: 7
Variable 'b' has wrong value. Expected: 48, Actual: 42"""
