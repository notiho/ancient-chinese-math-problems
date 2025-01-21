"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
答曰： a頃 ，奇 b步 。
"""

"""
Suppose there is a square field with a mulberry tree growing at the center. The distance from one corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

Answer: the field is *a* qing and *b* bu.
"""

from fractions import Fraction
import math

# 從角至桑，一百四十七步
corner_to_center = 147

# The diagonal of a square is related to its side length by the formula:
# diagonal = side * sqrt(2)
# Therefore, the side length of the square is:
side_length = Fraction(corner_to_center, math.sqrt(2))

# The area of the square field is:
area_in_bu = side_length**2

# Convert the area into qing and bu:
# 1 qing = 24000 bu
a = area_in_bu // 24000  # Number of qing
b = area_in_bu % 24000   # Remaining bu

a = Fraction(a)
b = Fraction(b)

a, b
"""
Code error: both arguments should be Rational instances"""
