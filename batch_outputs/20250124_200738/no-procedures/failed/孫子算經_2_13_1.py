"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
答曰： a頃 ，奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree planted at the center. The distance from one corner of the field to the mulberry tree is 147 bu.
Question: how large is the area of the field?

Answer: *a* qing, with a remainder of *b* bu.
"""

from fractions import Fraction
import math

# 從角至桑，一百四十七步
corner_to_center = 147

# The diagonal of a square is given by: diagonal = side * sqrt(2)
# Therefore, the side length of the square is:
side_length = Fraction(corner_to_center, math.sqrt(2))

# The area of the square is:
area_in_bu = side_length ** 2

# Convert the area into qing and bu (1 qing = 24000 bu)
a = area_in_bu // 24000  # Number of qing
b = area_in_bu % 24000   # Remaining bu

a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
