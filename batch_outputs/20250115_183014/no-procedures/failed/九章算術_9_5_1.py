"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
荅曰：水深 a丈 ；葭長 b丈 。
"""

"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at the center of the pond and extends 1 chi above the water surface. When the reed is pulled to the edge of the pond, it just touches the edge of the pond.

Question: How deep is the water, and how long is the reed?

Answer: The water depth is *a* zhang, and the reed length is *b* zhang.
"""

# Import Fraction to handle precise calculations
from fractions import Fraction

# Given:
pond_side = 1  # side length of the pond in zhang
reed_above_water = Fraction(1, 10)  # reed extends 1 chi above water, which is 1/10 zhang

# Let the water depth be "x" zhang, and the reed length be "y" zhang.
# Using the Pythagorean theorem:
# (reed length)^2 = (water depth + reed above water)^2 + (half the pond side)^2
# y^2 = (x + 1/10)^2 + (1/2)^2

# Solve for x (water depth) and y (reed length):
# Expand the equation:
# y^2 = (x + 1/10)^2 + (1/2)^2
# y^2 = (x + 1/10)^2 + 1/4
# y^2 = x^2 + 2x(1/10) + (1/10)^2 + 1/4
# y^2 = x^2 + (1/5)x + 1/100 + 1/4

# When the reed is pulled to the edge of the pond, the reed length y is equal to the hypotenuse:
# y^2 = x^2 + (1/2)^2
# x^2 + (1/5)x + 1/100 + 1/4 = x^2 + 1/4
# (1/5)x + 1/100 = 0
# (1/5)x = -1/100
# x = -1/100 * 
"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
