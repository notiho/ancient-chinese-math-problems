"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
荅曰：材徑 a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log buried in a wall, and its size is unknown. 
Using a measuring tool, it is pressed into the log to a depth of 1 cun, and the length of the chord (the straight line across the circle at that depth) is measured to be 1 chi.
Question: what is the diameter of the log?

Answer: the diameter of the log is *a* chi.
"""

# Given:
# Depth of the chord (distance from the surface to the chord) = 1 cun = 1/10 chi
depth = Fraction(1, 10)

# Length of the chord = 1 chi
chord_length = 1

# The relationship between the radius (r), depth (d), and chord length (c) is derived from geometry:
# r^2 = (c/2)^2 + (r - d)^2
# Expanding this equation:
# r^2 = (c/2)^2 + r^2 - 2rd + d^2
# Simplifying:
# 2rd = (c/2)^2 + d^2
# r = [(c/2)^2 + d^2] / (2d)

# Calculate the radius
radius = Fraction((chord_length / 2) ** 2 + depth ** 2, 2 * depth)

# Diameter is twice the radius
a = 2 * radius

# Result
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
