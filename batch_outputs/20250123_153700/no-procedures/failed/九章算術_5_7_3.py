"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question: What is the total volume of the trench?

Answer: The volume is *a* cubic chi.
"""

# Convert all dimensions to chi (1 zhang = 10 chi, 1 chi = 10 cun)

# Top width: 1 zhang 6 chi 3 cun
top_width = 10 + 6 + Fraction(3, 10)

# Bottom width: 1 zhang
bottom_width = 10

# Depth: 6 chi 3 cun
depth = 6 + Fraction(3, 10)

# Length: 13 zhang 2 chi 1 cun
length = 13 * 10 + 2 + Fraction(1, 10)

# Volume formula for a trapezoidal prism: V = (1/2) * (top_width + bottom_width) * depth * length
a = Fraction(1, 2) * (top_width + bottom_width) * depth * length

# The volume is `a` cubic chi.
"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
