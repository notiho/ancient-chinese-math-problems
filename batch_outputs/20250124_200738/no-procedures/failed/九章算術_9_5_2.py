"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
荅曰：水深 a丈 ；葭長 b丈 。
"""

#----- content starts here -----
"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at the center of the pond and extends 1 chi above the water. When the reed is pulled to the edge of the pond, it just touches the edge of the pond.

Question: How deep is the water, and how long is the reed?

Answer: The water depth is *a* zhang, and the reed length is *b* zhang.
"""

# Importing Fraction for precise calculations
from fractions import Fraction

# Side length of the pond (1 zhang)
pond_side = 1  # in zhang

# The reed extends 1 chi above the water, convert to zhang
reed_above_water = Fraction(1, 10)  # 1 chi = 1/10 zhang

# Let the water depth be "x" (in zhang)
# The reed length is "x + 1/10" (water depth + the part above water)

# Using the Pythagorean theorem:
# The distance from the center of the pond to the edge is half the diagonal of the square pond
# Diagonal of the square pond = sqrt(pond_side^2 + pond_side^2)
# Half the diagonal = sqrt(1^2 + 1^2) / 2 = sqrt(2) / 2

# When the reed is pulled to the edge, the hypotenuse of the triangle is the reed length
# Hypotenuse = sqrt((water depth)^2 + (half the diagonal)^2)

# Equation: (reed length)^2 = (water depth)^2 + (half the diagonal)^2
# (x + 1/10)^2 = x^2 + (sqrt(2)/2)^2

# Solve for x (water depth):
# Expand the equation:
# (x + 1/10)^2 = x^2 + (1/2)
# x^2 + 2x(1/10) + (1/10)^2 = x^2 + 1/2
# 2x(1/10) + (1/10)^2 = 1/2
# 2x(1/10) = 1/2 - (1/10)^2
# x = [1/2 - (1/10)^2] / (2/10)

# Simplify:
reed_above_water_squared = reed_above_water**2  # (1/10)^2
half_diagonal_squared = Fraction(1, 2)  # (sqrt(2)/2)^2 = 1/2
water_depth = (half_diagonal_squared - reed_above_water_squared) / (2 * reed_above_water)

# Calculate reed length:
reed_length = water_depth + reed_above_water

# Results:
a = water_depth  # Water depth in zhang
b = reed_length  # Reed length in zhang

a, b  # Output the results#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 49/20
Variable 'b' has wrong value. Expected: 13/10, Actual: 51/20"""
