"""
今有腰鼓田從八十二步两頭各廣三十步中央廣十二步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a waist-drum-shaped field (a trapezoidal field) with a length of 82 bu.
The two ends are each 30 bu wide, and the middle is 12 bu wide.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Field dimensions
length = 82  # 從八十二步
end_width = 30  # 两头各广三十步
middle_width = 12  # 中央广十二步

# Calculate the average width using the formula for a waist-drum-shaped field:
# Average width = (end_width + middle_width + end_width) / 3
average_width = Fraction(end_width + middle_width + end_width, 3)

# Calculate the area in bu²
area_in_bu_squared = length * average_width

# Convert the area to mu and remaining bu:
# 1 mu = 240 bu²
a = area_in_bu_squared // 240  # Whole mu
b = area_in_bu_squared % 240  # Remaining bu

# Output the result
a, b
"""
"""
