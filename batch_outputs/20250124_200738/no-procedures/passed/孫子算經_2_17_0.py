"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is a ditch with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate how many cubic units (fang) it contains, where 1000 cubic chi (cubic feet) make one fang.

Question: how many fang does it contain?

Answer: *a* fang.
"""

# 溝的尺寸
廣 = 10  # zhang
深 = 5   # zhang
長 = 20  # zhang

# 1 zhang = 10 chi, so convert all dimensions to chi
廣_尺 = 廣 * 10
深_尺 = 深 * 10
長_尺 = 長 * 10

# Calculate the total volume in cubic chi
體積_尺 = 廣_尺 * 深_尺 * 長_尺

# Convert cubic chi to fang (1000 cubic chi = 1 fang)
a = Fraction(體積_尺, 1000)  # result in fang

a#----- content ends here -----

"""
"""
