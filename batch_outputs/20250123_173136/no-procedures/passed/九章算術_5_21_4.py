"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a truncated prism (a frustum) with the following dimensions:
- Bottom width: 6 chi
- Top width: 10 chi (1 zhang = 10 chi)
- Depth: 3 chi
- End width: 8 chi
- No depth at the end
- Length: 7 chi

Question: What is the volume?

Answer: The volume is *a* cubic chi.
"""

# 下廣 (bottom width) = 6 chi
下廣 = 6

# 上廣 (top width) = 10 chi
上廣 = 10

# 深 (depth) = 3 chi
深 = 3

# 末廣 (end width) = 8 chi
末廣 = 8

# 無深 (no depth at the end) = 0 chi
無深 = 0

# 袤 (length) = 7 chi
袤 = 7

# Formula for the volume of a truncated prism:
# Volume = (1/6) * 袤 * (下廣 + 上廣 + 末廣) * 深
a = Fraction(1, 6) * 袤 * (下廣 + 上廣 + 末廣) * 深

# The result is the volume in cubic chi.
a
"""
"""
