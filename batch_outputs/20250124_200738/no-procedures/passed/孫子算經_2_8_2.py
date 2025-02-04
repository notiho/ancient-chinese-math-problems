"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a house foundation with a length of 3 zhang (south to north) and a width of 6 zhang (east to west). 
It is desired to build it with bricks and tiles, where every 2 cubic chi requires 5 bricks.
Question: how many bricks are needed in total?

Answer: *a* bricks.
"""

# Dimensions of the house foundation
南北 = 3 * 10  # Convert zhang to chi
東西 = 6 * 10  # Convert zhang to chi

# Height of the wall (assumed to be 1 chi unless otherwise stated)
高度 = 1  # chi

# Total volume of the wall in cubic chi
體積 = 南北 * 東西 * 高度

# Bricks required for every 2 cubic chi
每二尺用磚 = 5

# Calculate total bricks needed
a = Fraction(體積, 2) * 每二尺用磚#----- content ends here -----

"""
"""
