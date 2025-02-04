"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is an excavation with the following dimensions:
- Length (袤): 1 zhang 6 chi (16 chi),
- Depth (深): 1 zhang (10 chi),
- Top width (上廣): 6 chi,
- Total volume of the excavation (垣積): 576 cubic chi.

Question: What is the bottom width (穿地下廣)?

Answer: The bottom width is *a* chi.
"""

# Given dimensions
length = 16  # in chi
depth = 10  # in chi
top_width = 6  # in chi
volume = 576  # in cubic chi

# Formula for the volume of a trapezoidal prism:
# Volume = (1/2) * (top_width + bottom_width) * depth * length
# Solving for bottom_width:
# bottom_width = (2 * Volume / (depth * length)) - top_width

a = Fraction(2 * volume, depth * length) - top_width

# The bottom width (a) is calculated in chi.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 18/5, Actual: 6/5"""
