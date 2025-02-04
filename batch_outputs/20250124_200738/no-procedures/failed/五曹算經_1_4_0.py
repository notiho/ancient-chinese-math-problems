"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a waist drum-shaped field. The length (from) is 82 bu, the width at both ends is 30 bu, and the width at the center is 12 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

# Import Fraction to handle non-integer values
from fractions import Fraction

# Given dimensions
length = 82  # 從 (length)
end_width = 30  # 两头广 (width at both ends)
center_width = 12  # 中央广 (width at the center)

# Calculate the average width using the formula for a waist drum-shaped field
average_width = Fraction(end_width + center_width, 2)

# Calculate the area in bu²
area_in_bu = length * average_width

# Convert the area into mu and remaining bu
a = area_in_bu // 240  # 1 mu = 240 bu²
b = area_in_bu % 240  # Remaining bu²

# Output the result
a, b  # a is the number of mu, b is the remaining bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 8, Actual: 7
Variable 'b' has wrong value. Expected: 48, Actual: 42"""
