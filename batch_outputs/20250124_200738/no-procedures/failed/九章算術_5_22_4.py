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

Question: what is the volume of the roof?

Answer: *a* cubic chi.
"""

# Dimensions in zhang
下廣 = 3  # Bottom width in zhang
袤 = 4    # Bottom length in zhang
上袤 = 2  # Top length in zhang
高 = 1    # Height in zhang

# Convert zhang to chi (1 zhang = 10 chi)
下廣 = 下廣 * 10
袤 = 袤 * 10
上袤 = 上袤 * 10
高 = 高 * 10

# Volume formula for a truncated prism: V = (1/2) * 高 * (下底面積 + 上底面積)
# Here, 下底面積 = 下廣 * 袤, 上底面積 = 上袤 * 0 (since no width at the top)
下底面積 = 下廣 * 袤
上底面積 = 上袤 * 0

# Calculate the volume
a = Fraction(1, 2) * 高 * (下底面積 + 上底面積)  # Volume in cubic chi

a  # Output the result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5000, Actual: 6000"""
