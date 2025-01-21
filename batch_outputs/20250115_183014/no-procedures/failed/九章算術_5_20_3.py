"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a truncated pyramid-like object (a frustum) with the following dimensions:
- The bottom width is 5 chi.
- The bottom length is unknown.
- The top length is 4 chi.
- The top width is unknown.
- The height is 7 chi.

Question: What is the volume of this object?

Answer: The volume is *a* cubic chi.
"""

# Bottom width (下廣)
下廣 = 5

# Top length (上袤)
上袤 = 4

# Height (高)
高 = 7

# Formula for the volume of a frustum:
# V = (1/3) * 高 * (下廣^2 + 下廣 * 上袤 + 上袤^2)

a = Fraction(1, 3) * 高 * (下廣**2 + 下廣 * 上袤 + 上袤**2)
"""
Variable 'a' has wrong value. Expected: 70/3, Actual: 427/3"""
