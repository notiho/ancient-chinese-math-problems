"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
答曰： a頃 奇 b步 。
"""

"""
Suppose there is a square field with a mulberry tree in the center. The distance from one corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

Answer: *a* qing and *b* bu.
"""

# From the problem, the diagonal of the square field is 147 bu.
diagonal = 147

# The relationship between the diagonal and the side of a square is: diagonal = side * sqrt(2).
# Therefore, the side of the square can be calculated as:
side = Fraction(diagonal, 2**0.5)  # Using the square root of 2.

# The area of the square field is side^2.
area_in_bu = side * side

# Convert the area into qing and bu.
# 1 qing = 24000 bu.
a = area_in_bu // 24000  # Integer part in qing.
b = area_in_bu % 24000  # Remainder in bu.
"""
Code error: both arguments should be Rational instances"""
