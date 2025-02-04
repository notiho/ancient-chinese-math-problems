"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
答曰： a枚 。
"""

"""
Suppose there is a house foundation with a length of 3 zhang (north-south) and a width of 6 zhang (east-west).
It is desired to build it with bricks and tiles. For every 2 cubic chi, 5 bricks are used.
Question: how many bricks are needed?

Answer: *a* bricks.
"""

# Dimensions of the house foundation
南北 = 3 * 10  # Convert zhang to chi
東西 = 6 * 10  # Convert zhang to chi

# Height of the wall (in chi)
高度 = 2

# Volume of the wall (in cubic chi)
體積 = 南北 * 東西 * 高度

# Bricks required per 2 cubic chi
每二尺用磚 = 5

# Total bricks needed
a = Fraction(體積, 2) * 每二尺用磚
"""
Variable 'a' has wrong value. Expected: 4500, Actual: 9000"""
