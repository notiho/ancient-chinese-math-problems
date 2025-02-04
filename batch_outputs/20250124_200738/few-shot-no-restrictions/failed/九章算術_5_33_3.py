"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a width of 3 zhang and a length of 4 zhang 5 chi. It can hold 10,000 hu of grain.
Question: how tall is the granary?

The procedure says: Place the 10,000 hu of grain, converted to cubic chi, as the dividend.
Multiply the width and length to obtain the divisor.
Divide the dividend by the divisor to obtain the height in chi.

Answer: *a* zhang.
"""

from fractions import Fraction

# Given values
廣 = 3  # Width in zhang
袤 = 4 + Fraction(5, 10)  # Length in zhang (4 zhang 5 chi = 4.5 zhang)
容粟 = 10000  # Volume in hu

# Conversion: 1 hu = 10 cubic chi
容粟積尺 = 容粟 * 10  # Convert hu to cubic chi

# 廣袤相乘為法
法 = 廣 * 袤  # Width × Length in zhang^2

# 實如法而一，得高尺
高尺 = Fraction(容粟積尺, 法)  # Height in chi

# Convert height from chi to zhang (1 zhang = 10 chi)
a = 高尺 / 10  # Height in zhang

a  # Output the height in zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
