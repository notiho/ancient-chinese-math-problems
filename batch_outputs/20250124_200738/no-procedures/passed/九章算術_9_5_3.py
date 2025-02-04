"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
荅曰：水深 a丈 ；葭長 b丈 。
"""

#----- content starts here -----
"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at the center of the pond and extends 1 chi above the water. When the reed is pulled to the edge of the pond, it just touches the edge of the pond. 

Question: What is the depth of the water and the length of the reed?

Answer: The water depth is *a* zhang, and the reed length is *b* zhang.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# Side length of the pond (in zhang)
pond_side = 1  # 1 zhang

# The reed extends 1 chi above the water (1 chi = 1/10 zhang)
reed_above_water = Fraction(1, 10)  # 1 chi = 1/10 zhang

# The reed forms a right triangle when pulled to the edge of the pond.
# Hypotenuse: length of the reed
# One leg: depth of the water
# Other leg: half the side length of the pond (since the reed is at the center)

# Let water_depth = x (in zhang)
# Then reed_length = x + reed_above_water

# Using the Pythagorean theorem:
# (reed_length)^2 = (water_depth)^2 + (pond_side / 2)^2
# (x + reed_above_water)^2 = x^2 + (pond_side / 2)^2

# Substitute values and solve:
# (x + 1/10)^2 = x^2 + (1/2)^2
# Expand both sides:
# x^2 + 2x(1/10) + (1/10)^2 = x^2 + (1/2)^2
# Simplify:
# 2x(1/10) + (1/10)^2 = (1/2)^2
# 2x(1/10) = (1/2)^2 - (1/10)^2
# x = [(1/2)^2 - (1/10)^2] / (2 * 1/10)

# Calculate:
water_depth = Fraction((Fraction(1, 2) ** 2) - (Fraction(1, 10) ** 2), 2 * Fraction(1, 10))

# Reed length:
reed_length = water_depth + reed_above_water

# Final results:
a = water_depth  # Water depth in zhang
b = reed_length  # Reed length in zhang

a, b  # Output the results#----- content ends here -----

"""
"""
