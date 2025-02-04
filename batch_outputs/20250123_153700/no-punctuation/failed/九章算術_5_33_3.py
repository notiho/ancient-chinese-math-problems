"""
今有倉廣三丈袤四丈五尺容粟一萬斛問高幾何
術曰置粟一萬斛積尺為實廣袤相乘為法實如法而一得高尺
荅曰 a丈 
"""

"""
Suppose there is a granary with a width of 3 zhang and a length of 4 zhang 5 chi. It can hold 10,000 hu of grain.
Question: how tall is the granary?

The procedure says: Place the 10,000 hu of grain, convert it to cubic chi, and take it as the dividend.
Multiply the width and length to obtain the divisor.
Divide the dividend by the divisor to obtain the height in chi.

The answer says: *a* zhang.
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

# 實如法而一得高尺
高尺 = Fraction(粟積尺, 法)

# Convert chi to zhang (1 zhang = 10 chi)
a = Fraction(高尺, 10)  # Height in zhang
"""
Variable 'a' has wrong value. Expected: 2, Actual: 200/27"""
