"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a ditch with the following dimensions:
- Top width: 1 zhang 5 chi (15 chi)
- Bottom width: 1 zhang (10 chi)
- Depth: 5 chi
- Length: 7 zhang (70 chi)

Question: What is the volume of the ditch?

Answer: *a* cubic chi.
"""

# Define dimensions
top_width = 15  # in chi
bottom_width = 10  # in chi
depth = 5  # in chi
length = 70  # in chi

# Volume formula for a trapezoidal prism: V = (1/2) * (top_width + bottom_width) * depth * length
a = Fraction(1, 2) * (top_width + bottom_width) * depth * length

# Result
a  # Volume in cubic chi
"""
"""
