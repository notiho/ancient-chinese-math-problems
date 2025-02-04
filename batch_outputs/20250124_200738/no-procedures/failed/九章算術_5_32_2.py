"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is an excavation with the following dimensions:
- Length (袤): 1 zhang 6 chi = 16 chi
- Depth (深): 1 zhang = 10 chi
- Top width (上廣): 6 chi
The total volume of the excavation is 576 cubic chi.

Question: What is the bottom width (下廣) of the excavation?

Answer: The bottom width is *a* chi.
"""

# Given dimensions
length = 16  # chi
depth = 10  # chi
top_width = 6  # chi
volume = 576  # cubic chi

# Formula for the volume of a trapezoidal prism:
# Volume = (1/2) * (top_width + bottom_width) * depth * length
# Solve for bottom_width:
# bottom_width = (2 * Volume / (depth * length)) - top_width

a = Fraction(2 * volume, depth * length) - top_width
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 18/5, Actual: 6/5"""
