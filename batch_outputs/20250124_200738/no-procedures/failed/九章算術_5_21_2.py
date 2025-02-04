"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a truncated prism (a frustum) with the following dimensions:
- Bottom width: 6 chi
- Top width: 10 chi (1 zhang = 10 chi)
- Depth: 3 chi
- Narrow end width: 8 chi
- No depth at the narrow end
- Length: 7 chi

Question: What is the volume of this shape?

Answer: The volume is *a* cubic chi.
"""

# 下廣 (bottom width) = 6 尺
下廣 = 6

# 上廣 (top width) = 1 丈 = 10 尺
上廣 = 10

# 深 (depth) = 3 尺
深 = 3

# 末廣 (narrow end width) = 8 尺
末廣 = 8

# 無深 (no depth at the narrow end) = 0
末深 = 0

# 袤 (length) = 7 尺
袤 = 7

# Formula for the volume of a truncated prism:
# V = 袤 * ( (下廣 * 深) + (上廣 * 深) + (末廣 * 末深) ) / 3

a = Fraction(袤 * ((下廣 * 深) + (上廣 * 深) + (末廣 * 末深)), 3)

# The result is the volume in cubic chi.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 84, Actual: 112"""
