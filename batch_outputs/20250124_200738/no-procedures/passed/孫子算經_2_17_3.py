"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is a ditch with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate how many "fang" (cubic units) it makes, where 1 fang = 1000 cubic chi.

Question: How many fang does it make?

Answer: It makes *a* fang.
"""

# 溝的尺寸
廣 = 10  # zhang
深 = 5   # zhang
長 = 20  # zhang

# 1 zhang = 10 chi, so convert all dimensions to chi
廣_in_chi = 廣 * 10
深_in_chi = 深 * 10
長_in_chi = 長 * 10

# Calculate the total volume in cubic chi
total_volume_in_chi = 廣_in_chi * 深_in_chi * 長_in_chi

# Convert cubic chi to fang (1 fang = 1000 cubic chi)
a = Fraction(total_volume_in_chi, 1000)

# Result
a#----- content ends here -----

"""
"""
