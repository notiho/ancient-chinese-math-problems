"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
答曰： a枚 。
"""

"""
Suppose there is a house foundation with dimensions: 3 zhang (south to north) and 6 zhang (east to west). 
It is desired to build it with bricks and tiles. For every 2 cubic chi, 5 bricks are used.
Question: how many bricks are needed?

Answer: *a* bricks.
"""

# Dimensions of the house foundation
南北 = 3  # in zhang
東西 = 6  # in zhang

# Convert dimensions to chi (1 zhang = 10 chi)
南北 = 南北 * 10
東西 = 東西 * 10

# Height of the wall (assumed to be 1 chi for simplicity)
高度 = 1  # in chi

# Total volume of the wall in cubic chi
體積 = 南北 * 東西 * 高度

# Bricks required for every 2 cubic chi
每二尺用磚 = 5

# Total number of bricks required
a = Fraction(體積 * 每二尺用磚, 2)  # Total bricks needed

a
"""
"""
