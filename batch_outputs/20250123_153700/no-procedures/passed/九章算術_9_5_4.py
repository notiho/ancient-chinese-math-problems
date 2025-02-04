"""
今有池方一丈，葭生其中央，出水一尺。引葭赴岸，適與岸齊。問︰水深、葭長各幾何？
荅曰：水深 a丈 ；葭長 b丈 。
"""

"""
Suppose there is a square pond with a side length of 1 zhang. A reed grows at the center of the pond and extends 1 chi above the water surface. When the reed is pulled to the edge of the pond, it just touches the edge of the pond.

Question: How deep is the water, and how long is the reed?

Answer: The water depth is *a* zhang, and the reed length is *b* zhang.
"""

# Using the Pythagorean theorem:
# Let the water depth be `x` (in zhang), and the reed length be `y` (in zhang).
# The reed forms a right triangle when pulled to the edge of the pond:
# Hypotenuse = y (reed length)
# One leg = x (water depth)
# Other leg = 1/2 zhang (half the pond's side length)

# The reed also extends 1 chi above the water, so:
# y = x + 1/10 (since 1 chi = 1/10 zhang)

# Using the Pythagorean theorem:
# y^2 = x^2 + (1/2)^2

from fractions import Fraction
from math import sqrt

# Solve the equations:
# y = x + 1/10
# y^2 = x^2 + (1/2)^2

# Step 1: Substitute y = x + 1/10 into y^2 = x^2 + (1/2)^2
# (x + 1/10)^2 = x^2 + (1/2)^2
# Expand:
# x^2 + 2(x)(1/10) + (1/10)^2 = x^2 + (1/2)^2
# Simplify:
# 2(x)(1/10) + (1/10)^2 = (1/2)^2
# 2x/10 + 1/100 = 1/4
# Simplify further:
# x/5 + 1/100 = 25/100
# x/5 = 24/100
# x = (24/100) * 5
# x = 120/100 = 6/5

# Step 2: Solve for y using y = x + 1/10
x = Fraction(6, 5)  # Water depth in zhang
y = x + Fraction(1, 10)  # Reed length in zhang

# Final results:
a = x  # Water depth
b = y  # Reed length

a, b  # Output water depth and reed length
"""
"""
