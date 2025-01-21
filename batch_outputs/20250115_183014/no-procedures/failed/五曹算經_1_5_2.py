"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a drum-shaped field (鼓田) where both ends are 40 bu wide, the middle is 52 bu wide, and the length is 85 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Dimensions of the field
end_width = 40  # Width at both ends (bu)
middle_width = 52  # Width at the middle (bu)
length = 85  # Length of the field (bu)

# The area of a drum-shaped field is calculated as:
# Area = ( (end_width + middle_width) / 2 ) * length
area_in_bu = Fraction((end_width + middle_width), 2) * length

# Convert the area into mu and remaining bu
# 1 mu = 240 bu
a = area_in_bu // 240  # Whole mu
b = area_in_bu % 240  # Remaining bu

a, b  # Output the result as (a mu, b bu)
"""
Variable 'a' has wrong value. Expected: 15, Actual: 16
Variable 'b' has wrong value. Expected: 140, Actual: 70"""
