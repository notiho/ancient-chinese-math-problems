"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
荅曰：材徑 a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log buried in a wall, and its size is unknown. 
Using a measuring tool, it is found that when the tool is inserted 1 cun deep into the wall, the chord length (distance across the circle at that depth) is 1 chi.
Question: what is the diameter of the log?

Answer: the diameter of the log is *a* chi.
"""

# Given values
depth = Fraction(1, 10)  # 1 cun = 1/10 chi
chord_length = 1  # 1 chi

# The relationship between the radius (r), depth (d), and chord length (c) is derived from geometry:
# r^2 = (c/2)^2 + (r - d)^2
# Expanding and solving for r:
# r^2 = (c/2)^2 + r^2 - 2rd + d^2
# 2rd = (c/2)^2 + d^2
# r = [(c/2)^2 + d^2] / (2d)

radius = Fraction((chord_length / 2) ** 2 + depth ** 2, 2 * depth)

# Diameter is twice the radius
a = 2 * radius

a  # Diameter of the log in chi#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
