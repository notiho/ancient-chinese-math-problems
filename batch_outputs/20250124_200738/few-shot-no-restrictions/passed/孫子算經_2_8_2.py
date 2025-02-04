"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a building foundation, with a length of 3 zhang (north-south) and a width of 6 zhang (east-west). 
It is desired to build it using bricks and tiles. For every 2 cubic chi, 5 bricks are used.
Question: how many bricks are needed in total?

The procedure says: Place the east-west length (6 zhang), multiply it by the north-south length (3 zhang), obtaining 1800 cubic chi.
Multiply this by 5, obtaining 9000. Divide it by 2, and the result is the total number of bricks.

Answer: *a* bricks.
"""

# Dimensions of the foundation
南北 = 3  # in 丈
東西 = 6  # in 丈

# Conversion factor: 1 丈 = 10 尺
丈_to_尺 = 10

# Convert dimensions to 尺
南北_in_尺 = 南北 * 丈_to_尺
東西_in_尺 = 東西 * 丈_to_尺

# Calculate the total volume in cubic 尺
體積 = 南北_in_尺 * 東西_in_尺  # 平方尺 (area)
體積 *= 1  # Assuming height is 1 尺 (not explicitly mentioned)

# For every 2 cubic 尺, 5 bricks are used
每二尺用磚 = 5
每尺用磚 = 每二尺用磚 / 2

# Calculate the total number of bricks
a = 體積 * 每尺用磚

a  # Total number of bricks#----- content ends here -----

"""
"""
