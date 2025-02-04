"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a(=2)丈 。
"""

"""
Suppose there is a granary with a width of 3 zhang and a length of 4 zhang 5 chi. It holds 10,000 hu of grain.
Question: how tall is it?

The procedure says: Place the 10,000 hu of grain as the volume in cubic chi, which becomes the dividend.
Multiply the width and length to obtain the divisor.
Divide the dividend by the divisor to obtain the height in chi.

Answer: *a*(=2) zhang.
"""

# 廣三丈
廣 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 袤四丈五尺
袤 = 4 * 10 + 5  # Convert zhang and chi to chi

# 容粟一萬斛
粟 = 10000

# 1 hu = 10 cubic chi
粟積尺 = 粟 * 10  # Convert hu to cubic chi

# 廣袤相乘為法
法 = 廣 * 袤

# 實如法而一，得高尺
高尺 = Fraction(粟積尺, 法)

# Convert chi to zhang
a = 高尺 / 10  # 2 zhang
"""
Variable 'a' has wrong value. Expected: 2, Actual: 200/27"""
