"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a truncated pyramid (a frustum) with:
- Bottom width (lower base) = 5 chi,
- Bottom length = 0 chi (not given, assume square base),
- Top length (upper base) = 4 chi,
- Top width = 0 chi (not given, assume square base),
- Height = 7 chi.

Question: What is the volume of the frustum?

Answer: The volume is *a* cubic chi.
"""

# Bottom base area (square base)
下底面積 = 5 * 5  # 5 chi by 5 chi

# Top base area (square base)
上底面積 = 4 * 4  # 4 chi by 4 chi

# Height of the frustum
高 = 7

# Volume of a frustum formula: V = (1/3) * 高 * (下底面積 + 上底面積 + sqrt(下底面積 * 上底面積))
a = Fraction(1, 3) * 高 * (下底面積 + 上底面積 + (下底面積 * 上底面積) ** 0.5)

a
"""
Variable 'a' has wrong value. Expected: 70/3, Actual: 142.33333333333334"""
