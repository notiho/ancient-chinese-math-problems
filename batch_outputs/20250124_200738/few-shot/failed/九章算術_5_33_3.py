"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a width of 3 zhang and a length of 4 zhang 5 chi. It holds 10,000 hu of grain.
Question: how high is the granary?

The procedure says: Place the 10,000 hu of grain as the volume in chi, which becomes the dividend.
Multiply the width and length together to form the divisor.
Divide the dividend by the divisor to obtain the height in chi.

Answer: *a* zhang.
"""

# 廣三丈
廣 = 3

# 袤四丈五尺 (convert to zhang: 1 zhang = 10 chi)
袤 = 4 + Fraction(5, 10)

# 容粟一萬斛 (convert hu to cubic chi: 1 hu = 10 cubic chi)
粟 = 10000 * 10

# 置粟一萬斛積尺為實
實 = 粟

# 廣袤相乘為法
法 = 廣 * 袤

# 實如法而一，得高尺
高 = Fraction(實, 法)

# Convert height to zhang (1 zhang = 10 chi)
a = Fraction(高, 10)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
