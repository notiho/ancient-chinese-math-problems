"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a house foundation, 3 zhang from south to north and 6 zhang from east to west.
It is desired to build it with bricks and tiles, where every 2 cubic chi requires 5 bricks.
Question: how many bricks are needed?

The procedure says: Place the east-west length (6 zhang), multiply it by the south-north length (3 zhang), obtaining 1800 cubic chi.
Multiply this by 5, obtaining 9000.
Divide it by 2, and the result is the number of bricks.

Answer: *a* bricks.
"""

from fractions import Fraction

# Dimensions of the house foundation
南北 = 3  # in zhang
東西 = 6  # in zhang

# Conversion: 1 zhang = 10 chi
南北 = 南北 * 10  # in chi
東西 = 東西 * 10  # in chi

# Volume of the foundation in cubic chi
體積 = 南北 * 東西  # 平方 chi (area)
體積 = 體積 * 1  # Assuming height is 1 chi for simplicity

# Every 2 cubic chi requires 5 bricks
每二尺需磚 = 5
每一尺需磚 = Fraction(每二尺需磚, 2)

# Total number of bricks
a = 體積 * 每一尺需磚

a#----- content ends here -----

"""
"""
