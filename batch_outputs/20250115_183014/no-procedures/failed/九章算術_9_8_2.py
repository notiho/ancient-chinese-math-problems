"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
荅曰：材徑 a尺 。
"""

"""
Suppose there is a cylindrical object (round timber) embedded in a wall, and its size is unknown.
Using a measuring tool, it is pressed into the wall to a depth of 1 cun, and the chord length of the circular cross-section is measured to be 1 chi.
Question: what is the diameter of the cylinder?

Answer: the diameter of the cylinder is *a* chi.
"""

# Given values
depth = Fraction(1, 10)  # 1 cun = 1/10 chi
chord_length = 1  # in chi

# The relationship between the radius (r), depth (d), and chord length (c) is derived from geometry:
# r^2 = (c/2)^2 + (r - d)^2
# Expanding and simplifying:
# r^2 = (c/2)^2 + r^2 - 2rd + d^2
# 0 = (c/2)^2 - 2rd + d^2
# Solving for r:
# r = [(c/2)^2 + d^2] / (2d)

radius = Fraction((chord_length / 2) ** 2 + depth ** 2, 2 * depth)

# Diameter is twice the radius
a = 2 * radius

a  # Diameter in chi
"""
Code error: both arguments should be Rational instances"""
