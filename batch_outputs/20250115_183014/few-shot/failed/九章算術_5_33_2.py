"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

"""
Suppose there is a granary with a width of 3 zhang and a length of 4 zhang 5 chi. It holds 10,000 hu of millet.
Question: how tall is the granary?

The procedure says: Place the millet volume of 10,000 hu into cubic chi as the dividend.
Multiply the width and length to obtain the divisor.
Divide the dividend by the divisor to obtain the height in chi.

Answer: *a* zhang.
"""

# 廣三丈
廣 = 3  # in zhang

# 袤四丈五尺
袤 = 4 + Fraction(5, 10)  # Convert 5 chi to zhang (1 zhang = 10 chi)

# 容粟一萬斛
粟 = 10000  # in hu

# 1 hu = 10 cubic chi
粟積尺 = 粟 * 10  # Convert hu to cubic chi

# 廣袤相乘為法
法 = 廣 * 袤  # Width × Length

# 實如法而一，得高尺
高 = Fraction(粟積尺, 法)  # Height in chi

# Convert height to zhang (1 zhang = 10 chi)
a = 高 / 10  # Height in zhang
"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
