"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
答曰： a斛 奇 b分 。
"""

"""
Suppose there is a granary in the shape of a cone with a base circumference of 48 chi and a height of 6 chi.
Question: how much millet can it hold?

Answer: *a* hu and *b* fen.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Given dimensions
circumference = 48  # chi
height = 6  # chi

# Calculate the radius of the base
# Circumference = 2 * π * radius
# Using π = 3 (ancient approximation)
radius = Fraction(circumference, 2 * 3)

# Volume of a cone = (1/3) * π * r^2 * h
# Using π = 3
volume = Fraction(1, 3) * 3 * radius**2 * height

# Convert volume from cubic chi to hu
# 1 hu = 10 cubic chi
volume_in_hu = volume / 10

# Separate the integer part (a) and fractional part (b)
a = volume_in_hu.numerator // volume_in_hu.denominator  # Integer part (hu)
b = volume_in_hu - a  # Fractional part (fen)

# Convert fractional part to fen (1 hu = 10 fen)
b = b * 10  # Convert to fen

# Final result
a = Fraction(a)  # Integer part as a fraction
b = Fraction(b)  # Fractional part as a fraction

a, b  # Output the result as (a hu, b fen)
"""
Variable 'a' has wrong value. Expected: 316, Actual: 38
Variable 'b' has wrong value. Expected: 8, Actual: 4"""
