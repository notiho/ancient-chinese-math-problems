"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
答曰： a枚 。
"""

"""
Suppose there is a house foundation, 3 zhang from south to north, and 6 zhang from east to west.
It is desired to build it with bricks and tiles. For every 2 cubic chi, 5 bricks are used.
Question: how many bricks are needed in total?

Answer: *a* bricks.
"""

# Dimensions of the house foundation
南北 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)
東西 = 6 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# Height of the wall (in chi)
高度 = 2  # The wall is 2 chi thick

# Volume of the wall in cubic chi
體積 = 南北 * 東西 * 高度

# Bricks used per 2 cubic chi
每二尺用磚 = 5

# Total number of bricks needed
a = (體積 * 每二尺用磚) // 2  # Divide by 2 cubic chi and multiply by 5 bricks per unit

a
"""
Variable 'a' has wrong value. Expected: 4500, Actual: 9000"""
