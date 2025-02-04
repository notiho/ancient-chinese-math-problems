"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
荅曰：材徑 a尺 。
"""

"""
Suppose there is a round log buried in a wall, and its size is unknown. When drilled into, the depth is 1 cun, and the chord length (distance across the circle at that depth) is 1 chi.
Question: what is the diameter of the log?

Answer: the diameter of the log is *a* chi.
"""

# Depth of the drill (radius minus depth of chord) in cun
depth = 1  # 1 cun

# Chord length (distance across the circle at the depth) in chi
chord_length = 1  # 1 chi

# Convert depth to chi (1 chi = 10 cun)
depth_in_chi = Fraction(depth, 10)

# Using the geometry of a circle:
# (diameter / 2)^2 = (chord_length / 2)^2 + (diameter / 2 - depth_in_chi)^2
# Let r = diameter / 2, solve for r:
# r^2 = (chord_length / 2)^2 + (r - depth_in_chi)^2

# chord_length / 2
half_chord = Fraction(chord_length, 2)

# Expand the equation:
# r^2 = (half_chord)^2 + (r - depth_in_chi)^2
# r^2 = (half_chord)^2 + r^2 - 2 * r * depth_in_chi + (depth_in_chi)^2

# Simplify:
# 0 = (half_chord)^2 - 2 * r * depth_in_chi + (depth_in_chi)^2
# 2 * r * depth_in_chi = (half_chord)^2 + (depth_in_chi)^2
# r = [(half_chord)^2 + (depth_in_chi)^2] / (2 * depth_in_chi)

r = Fraction(half_chord**2 + depth_in_chi**2, 2 * depth_in_chi)

# Diameter is 2 * r
a = 2 * r

# Result
a
"""
"""
