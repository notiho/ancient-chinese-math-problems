"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a(=2)丈 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a width of 3 zhang and a length of 4 zhang 5 chi. It holds 10,000 hu of millet.
Question: how tall is it?

The procedure says: Place the 10,000 hu of millet as the volume in cubic chi, which becomes the dividend.
Multiply the width and length to obtain the divisor.
Divide the dividend by the divisor, obtaining the height in chi.

Answer: *a*(=2) zhang.
"""

# 廣三丈
廣 = 3  # in 丈

# 袤四丈五尺
袤 = 4 + Fraction(5, 10)  # 4丈5尺 = 4.5丈

# 容粟一萬斛
粟 = 10000  # in 斛

# 1斛 = 10立方尺
粟積尺 = 粟 * 10  # Convert to cubic chi

# 廣袤相乘為法
法 = 廣 * 袤  # in square zhang

# 實如法而一，得高尺
高尺 = Fraction(粟積尺, 法)  # in chi

# Convert 高尺 to 丈 (1丈 = 10尺)
a = 高尺 / 10  # 2丈#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
