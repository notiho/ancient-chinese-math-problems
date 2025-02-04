"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a width of 3 zhang and a length of 4 zhang 5 chi. It holds 10,000 hu of grain.
Question: how tall is the granary?

The procedure says: Place the 10,000 hu of grain as the volume in chi, which becomes the dividend.
Multiply the width and length together, which becomes the divisor.
Divide the dividend by the divisor, obtaining the height in chi.

Answer: *a* zhang.
"""

# 廣三丈
廣 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 袤四丈五尺
袤 = 4 * 10 + 5  # Convert zhang and chi to chi

# 容粟一萬斛
粟 = 10000

# 1斛 = 10立方尺, Convert hu to cubic chi
粟積 = 粟 * 10

# 廣袤相乘為法
法 = 廣 * 袤

# 實如法而一，得高尺
高 = Fraction(粟積, 法)

# Convert 高 from chi to zhang
a = Fraction(高, 10)  # 1 zhang = 10 chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 200/27"""
