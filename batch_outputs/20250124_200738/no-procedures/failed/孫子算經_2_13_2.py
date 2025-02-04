"""
今有方田桑生中央，從角至桑，一百四十七步。問：為田幾何？
答曰： a頃 ，奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a square field with a mulberry tree growing at its center. The distance from one corner of the field to the mulberry tree is 147 bu.
Question: How large is the area of the field?

Answer: The field is *a* qing and *b* bu².
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Distance from corner to the center (diagonal / 2)
diagonal_half = 147

# The diagonal of the square is twice this distance
diagonal = 2 * diagonal_half

# The relationship between the diagonal and the side of a square is:
# diagonal = side * sqrt(2)
# side = diagonal / sqrt(2)
# To avoid using sqrt(2), we use the approximation: sqrt(2) ≈ 1.414213562
side = Fraction(diagonal, 1.414213562)

# The area of the square is side²
area_in_bu2 = side * side

# Convert the area into qing and remaining bu²
# 1 qing = 24000 bu²
a = area_in_bu2 // 24000  # Number of qing
b = area_in_bu2 % 24000   # Remaining bu²

a, b  # Output the results#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
