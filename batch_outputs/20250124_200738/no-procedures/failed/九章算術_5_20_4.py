"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a truncated pyramid (a frustum) with the following dimensions:
- The bottom width is 5 chi.
- The bottom length is unknown.
- The top length is 4 chi.
- The top width is unknown.
- The height is 7 chi.

Question: What is the volume of this frustum?

Answer: The volume is *a* cubic chi.
"""

# 下廣 (bottom width) = 5 尺
下廣 = 5

# 上袤 (top length) = 4 尺
上袤 = 4

# 高 (height) = 7 尺
高 = 7

# Formula for the volume of a frustum:
# V = (1/3) * 高 * (底面積 + 頂面積 + sqrt(底面積 * 頂面積))
# Here, since the bottom length and top width are not given, we assume the frustum is symmetric and square-based.
# Thus, the bottom area = 下廣^2, and the top area = 上袤^2.

底面積 = 下廣**2
頂面積 = 上袤**2

# Calculate the volume
a = Fraction(1, 3) * 高 * (底面積 + 頂面積 + (底面積 * 頂面積)**0.5)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 70/3, Actual: 142.33333333333334"""
