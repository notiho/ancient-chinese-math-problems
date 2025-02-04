"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
術曰：置廣一十丈，以深五丈乘之，得五千尺，又以長二十丈乘之，得一百萬尺，以一千除之，即得。
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is a ditch with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate the volume in units where 1000 cubic chi make 1 fang.
Question: how many fang does it make?

The procedure says: Place the width of 10 zhang, multiply it by the depth of 5 zhang, obtaining 5000 cubic chi.
Then multiply it by the length of 20 zhang, obtaining 1,000,000 cubic chi.
Divide this by 1000, and the result is the volume in fang.

Answer: *a* fang.
"""

# Given dimensions
廣 = 10  # Width in zhang
深 = 5   # Depth in zhang
長 = 20  # Length in zhang

# Conversion factor: 1 zhang = 10 chi
zhang_to_chi = 10

# Convert dimensions to chi
廣_chi = 廣 * zhang_to_chi
深_chi = 深 * zhang_to_chi
長_chi = 長 * zhang_to_chi

# Calculate the volume in cubic chi
體積_cubic_chi = 廣_chi * 深_chi * 長_chi

# Conversion factor: 1000 cubic chi = 1 fang
cubic_chi_to_fang = 1000

# Convert the volume to fang
a = Fraction(體積_cubic_chi, cubic_chi_to_fang)

a  # The volume in fang#----- content ends here -----

"""
"""
