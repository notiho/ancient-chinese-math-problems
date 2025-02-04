"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a width of 3 zhang and a length of 4 zhang 5 chi. It holds 10,000 hu of grain.
Question: how tall is the granary?

The procedure says: Place the 10,000 hu of grain into cubic chi as the dividend.
Multiply the width and length to obtain the divisor.
Divide the dividend by the divisor to obtain the height in chi.

The answer says: *a* zhang.
"""

# 廣三丈
廣 = 3  # in 丈

# 袤四丈五尺
袤 = 4 + Fraction(5, 10)  # Convert 5 尺 to 丈 (1 丈 = 10 尺)

# 容粟一萬斛
粟 = 10000  # in 斛

# 1 斛 = 10 立方尺
粟積尺 = 粟 * 10  # Convert 粟 to cubic chi (積尺)

# 廣袤相乘為法
法 = 廣 * 袤  # Width × Length in 丈²

# 實如法而一，得高尺
高 = Fraction(粟積尺, 法)  # Height in chi (尺)

# Convert 高 from 尺 to 丈 (1 丈 = 10 尺)
a = 高 / 10  # Height in 丈#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
