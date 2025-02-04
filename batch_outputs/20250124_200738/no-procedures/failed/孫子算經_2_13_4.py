"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
答曰： a頃 ，奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree growing in the center. The distance from a corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

Answer: The field is *a* qing and *b* bu.
"""

from fractions import Fraction
import math

# 從角至桑，一百四十七步
distance_corner_to_center = 147

# The diagonal of the square field is twice the distance from the corner to the center
diagonal = 2 * distance_corner_to_center

# The side length of the square field can be calculated using the diagonal formula: diagonal = side * sqrt(2)
side_length = Fraction(diagonal, math.sqrt(2))

# The area of the square field is side_length^2
area_in_bu = side_length**2

# Convert the area into qing and bu
# 1 qing = 24000 bu
a = area_in_bu // 24000  # Integer part in qing
b = area_in_bu % 24000  # Remainder in bu

a = Fraction(a)
b = Fraction(b)

a, b#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
