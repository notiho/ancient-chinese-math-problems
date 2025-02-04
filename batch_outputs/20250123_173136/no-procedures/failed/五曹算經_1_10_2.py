"""
今有田桑生中央從隅至桑一百四十七步。問：為田㡬何？
答曰： a頃 奇 b步 。
"""

"""
Suppose there is a square field with a mulberry tree in the center. The distance from one corner of the field to the mulberry tree is 147 bu.
Question: how large is the field?

Answer: *a* qing and *b* bu.
"""

# From the problem, the distance from the corner to the center is the diagonal of the square field divided by 2.
# Let the side length of the square field be `s`. The diagonal of the square is `s * sqrt(2)`.
# Therefore, the diagonal divided by 2 equals 147 bu:
# s * sqrt(2) / 2 = 147
# Solving for `s`, we get:
# s = 147 * 2 / sqrt(2) = 147 * sqrt(2)

# Step 1: Calculate the side length of the square field.
from fractions import Fraction

# Distance from corner to center
corner_to_center = 147

# Side length of the square field
side_length = Fraction(147 * 2, 2**0.5)

# Step 2: Calculate the area of the square field.
# Area = side_length^2
area_in_bu = side_length**2

# Step 3: Convert the area into qing and bu.
# 1 qing = 24000 bu
qing = area_in_bu // 24000
remaining_bu = area_in_bu % 24000

# Final result
a = qing
b = remaining_bu

# Output the result
a, b
"""
Code error: both arguments should be Rational instances"""
