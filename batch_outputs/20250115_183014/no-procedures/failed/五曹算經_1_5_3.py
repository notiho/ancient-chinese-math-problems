"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a drum-shaped field (鼓田) where both ends are 40 bu wide, the middle is 52 bu wide, and the length is 85 bu.
Question: how large is the area of the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Two ends' width
end_width = 40

# Middle width
middle_width = 52

# Length of the field
length = 85

# Calculate the average width of the field
average_width = Fraction(end_width + middle_width, 2)

# Calculate the total area in square bu
total_area_bu = average_width * length

# Convert the total area into mu and remaining bu
a = total_area_bu // 240  # 1 mu = 240 square bu
b = total_area_bu % 240  # Remaining bu after converting to mu

# Output the result
a, b
"""
Variable 'a' has wrong value. Expected: 15, Actual: 16
Variable 'b' has wrong value. Expected: 140, Actual: 70"""
