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

Answer: The volume is *a* cubic chi.
"""

# Define the dimensions
top_width = 15  # in chi
bottom_width = 10  # in chi
depth = 5  # in chi
length = 70  # in chi

# The formula for the volume of a trapezoidal prism is:
# Volume = ((top_width + bottom_width) / 2) * depth * length
a = Fraction((top_width + bottom_width), 2) * depth * length

# Result: a is the volume in cubic chi.
"""
"""
