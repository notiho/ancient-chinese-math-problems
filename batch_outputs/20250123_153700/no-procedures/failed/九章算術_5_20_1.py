"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a truncated pyramid (a frustum) with the following dimensions:
- The bottom width is 5 chi.
- The bottom length is unknown.
- The top length is 4 chi.
- The top width is unknown.
- The height is 7 chi.

Question: What is the volume of the frustum?

Answer: The volume is *a* cubic chi.
"""

# Bottom width (下廣)
下廣 = 5

# Top length (上袤)
上袤 = 4

# Height (高)
高 = 7

# Volume of a frustum formula: V = (1/3) * 高 * (底面積 + 頂面積 + sqrt(底面積 * 頂面積))
# Since the bottom length and top width are unknown, assume they are equal to the given dimensions (下廣 and 上袤).

底面積 = 下廣 * 下廣  # Bottom area (assuming square base)
頂面積 = 上袤 * 上袤  # Top area (assuming square top)

# Calculate the volume
a = Fraction(1, 3) * 高 * (底面積 + 頂面積 + (底面積 * 頂面積) ** 0.5)

a
"""
Variable 'a' has wrong value. Expected: 70/3, Actual: 142.33333333333334"""
