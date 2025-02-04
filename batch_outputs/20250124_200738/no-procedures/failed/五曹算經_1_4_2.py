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

# Import Fraction for precise calculations
from fractions import Fraction

# Given dimensions
length = 82  # Length of the field in bu
end_width = 30  # Width at both ends in bu
middle_width = 12  # Width at the middle in bu

# Calculate the average width using the waist-drum formula
average_width = Fraction(end_width + middle_width, 2)

# Calculate the area in bu^2
area_in_bu2 = length * average_width

# Convert the area to mu and bu
# 1 mu = 240 bu^2
a = area_in_bu2 // 240  # Whole mu
b = area_in_bu2 % 240  # Remaining bu

# Output the result
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 8, Actual: 7
Variable 'b' has wrong value. Expected: 48, Actual: 42"""
