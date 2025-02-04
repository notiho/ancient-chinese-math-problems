"""
今有溝，廣十丈，深五丈，長二十丈，欲以千尺作一方。問：得幾何？
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is a trench with a width of 10 zhang, a depth of 5 zhang, and a length of 20 zhang.
It is desired to calculate the volume in units where 1000 cubic chi equals 1 fang (方).

Question: How many fang is the trench's volume?

Answer: *a* fang.
"""

# Dimensions of the trench
廣 = 10  # width in zhang
深 = 5   # depth in zhang
長 = 20  # length in zhang

# Convert dimensions from zhang to chi (1 zhang = 10 chi)
廣_尺 = 廣 * 10
深_尺 = 深 * 10
長_尺 = 長 * 10

# Calculate the volume in cubic chi
體積_尺 = 廣_尺 * 深_尺 * 長_尺

# Convert cubic chi to fang (1000 cubic chi = 1 fang)
a = Fraction(體積_尺, 1000)

# Output the result
a#----- content ends here -----

"""
"""
