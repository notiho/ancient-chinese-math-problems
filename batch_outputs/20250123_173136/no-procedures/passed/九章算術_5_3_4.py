"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a dam with the following dimensions:
- Bottom width: 2 zhang
- Top width: 8 chi
- Height: 4 chi
- Length: 12 zhang 7 chi

Question: What is the total volume?

Answer: *a* cubic chi.
"""

# Dimensions of the dam
bottom_width = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
top_width = 8  # Already in chi
height = 4  # Already in chi
length = 12 * 10 + 7  # Convert 12 zhang 7 chi to chi

# Formula for the volume of a trapezoidal prism: V = (1/2) * (bottom_width + top_width) * height * length
a = Fraction(1, 2) * (bottom_width + top_width) * height * length

# The result is in cubic chi
a
"""
"""
