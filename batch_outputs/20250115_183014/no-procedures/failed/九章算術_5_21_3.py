"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a truncated prism (a frustum). The bottom width is 6 chi, the top width is 10 chi, the depth is 3 chi, and the middle width is 8 chi (with no depth). The length is 7 chi.
Question: what is the volume?

Answer: the volume is *a* cubic chi.
"""

# 下廣 (bottom width) = 6 尺
下廣 = 6

# 上廣 (top width) = 10 尺
上廣 = 10

# 深 (depth) = 3 尺
深 = 3

# 末廣 (middle width) = 8 尺
末廣 = 8

# 袤 (length) = 7 尺
袤 = 7

# Formula for the volume of a truncated prism:
# Volume = (下廣 + 上廣 + 末廣) * 深 * 袤 / 3
a = Fraction((下廣 + 上廣 + 末廣) * 深 * 袤, 3)

# The result is the volume in cubic chi.
a
"""
Variable 'a' has wrong value. Expected: 84, Actual: 168"""
