"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a truncated prism (a frustum). The bottom width is 6 chi, the top width is 10 chi, the depth is 3 chi, and the middle width is 8 chi with no depth, and the length is 7 chi.
Question: what is the volume?

Answer: the volume is *a* cubic chi.
"""

# 下廣 (bottom width) = 6 chi
下廣 = 6

# 上廣 (top width) = 10 chi
上廣 = 10

# 末廣 (middle width) = 8 chi
末廣 = 8

# 深 (depth) = 3 chi
深 = 3

# 袤 (length) = 7 chi
袤 = 7

# The formula for the volume of a truncated prism is:
# V = (下廣 + 上廣 + 末廣) * 深 * 袤 / 3

a = Fraction((下廣 + 上廣 + 末廣) * 深 * 袤, 3)

# The volume is stored in variable `a`.
"""
Variable 'a' has wrong value. Expected: 84, Actual: 168"""
