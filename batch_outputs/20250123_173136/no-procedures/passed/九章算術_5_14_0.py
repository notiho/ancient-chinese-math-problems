"""
今有方亭，下方五丈，上方四丈，高五丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a square-based frustum (a truncated pyramid) with the following dimensions:
- The bottom side is 5 zhang,
- The top side is 4 zhang,
- The height is 5 zhang.

Question: What is the volume of the frustum?

Answer: The volume is *a* cubic chi.
"""

# Dimensions of the frustum
下方 = 5  # Bottom side in zhang
上方 = 4  # Top side in zhang
高 = 5    # Height in zhang

# Convert all dimensions to chi (1 zhang = 10 chi)
下方 = 下方 * 10
上方 = 上方 * 10
高 = 高 * 10

# Formula for the volume of a square-based frustum:
# Volume = (1/3) * 高 * (下方^2 + 下方 * 上方 + 上方^2)
a = Fraction(1, 3) * 高 * (下方**2 + 下方 * 上方 + 上方**2)

a  # The volume in cubic chi
"""
"""
