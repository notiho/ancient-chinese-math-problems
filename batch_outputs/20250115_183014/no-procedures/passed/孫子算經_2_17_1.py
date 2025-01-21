"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
答曰： a 方。
"""

"""
Suppose there is a ditch with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate how many cubic units (fang) it contains, where 1000 cubic chi (cubic feet) make 1 fang.

Question: how many fang does it contain?

Answer: *a* fang.
"""

# 溝的 dimensions
廣 = 10  # zhang
深 = 5   # zhang
長 = 20  # zhang

# Convert zhang to chi (1 zhang = 10 chi)
廣_in_chi = 廣 * 10
深_in_chi = 深 * 10
長_in_chi = 長 * 10

# Calculate the volume in cubic chi
體積_in_cubic_chi = 廣_in_chi * 深_in_chi * 長_in_chi

# Convert cubic chi to fang (1000 cubic chi = 1 fang)
a = Fraction(體積_in_cubic_chi, 1000)  # result in fang

a  # Output the result
"""
"""
