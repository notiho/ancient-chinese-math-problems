"""
今有鼓田两頭各廣四十步中央廣五十二步從八十五步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a drum-shaped field (鼓田) where the two ends are each 40 bu wide, the center is 52 bu wide, and the length is 85 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# Two ends' width
end_width = 40

# Central width
center_width = 52

# Length of the field
length = 85

# Formula for the area of a drum-shaped field:
# Area = ( (end_width + center_width) / 2 ) * length
area_in_bu = Fraction((end_width + center_width), 2) * length

# Convert the area into mu and remaining bu
# 1 mu = 240 bu
a = area_in_bu // 240  # Whole mu
b = area_in_bu % 240   # Remaining bu

a, b  # Output the result as (a mu, b bu)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15, Actual: 16
Variable 'b' has wrong value. Expected: 140, Actual: 70"""
