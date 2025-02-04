"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a thatched roof (芻甍) with the following dimensions:
- Bottom width: 3 zhang
- Bottom length: 4 zhang
- Top length: 2 zhang (no width at the top)
- Height: 1 zhang

Question: What is the volume of the roof?

Answer: *a* cubic chi.
"""

# Dimensions
下廣 = 3  # Bottom width in zhang
袤底 = 4  # Bottom length in zhang
袤頂 = 2  # Top length in zhang
高 = 1    # Height in zhang

# Convert all dimensions to chi (1 zhang = 10 chi)
下廣 *= 10
袤底 *= 10
袤頂 *= 10
高 *= 10

# The volume of a truncated prism is calculated as:
# V = (1/2) * 高 * (下底面積 + 上底面積)
# Here, 下底面積 = 下廣 * 袤底, and 上底面積 = 0 (since the top has no width)

下底面積 = 下廣 * 袤底
上底面積 = 0

# Volume in cubic chi
a = Fraction(1, 2) * 高 * (下底面積 + 上底面積)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5000, Actual: 6000"""
