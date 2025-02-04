"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
答曰： a頃 ，奇 b步 。
"""

"""
Suppose there is a square field with a mulberry tree planted at the center. The distance from any corner of the field to the mulberry tree is 147 bu.
Question: how large is the area of the field?

Answer: The field is *a* qing and *b* bu².
"""

from fractions import Fraction

# Distance from corner to the center (diagonal / 2)
diagonal_half = 147

# The full diagonal of the square
diagonal = 2 * diagonal_half

# The relationship between the diagonal and the side of a square is:
# diagonal = side * sqrt(2)
# side = diagonal / sqrt(2)
# Since we are working with areas, we can directly calculate the area as:
# area = (diagonal²) / 2

# Calculate the area of the square in bu²
area_bu2 = Fraction(diagonal**2, 2)

# Convert the area into qing and remaining bu²
# 1 qing = 24000 bu²
a = area_bu2 // 24000  # Number of qing
b = area_bu2 % 24000  # Remaining bu²

a, b  # Output the result as (qing, remaining bu²)
"""
Variable 'a' has wrong value. Expected: 183/100, Actual: 1
Variable 'b' has wrong value. Expected: 180, Actual: 19218"""
