"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a house foundation, 3 zhang from south to north, and 6 zhang from east to west.
It is desired to build it with bricks and tiles, where every 2 cubic chi requires 5 bricks.
Question: how many bricks are needed?

The procedure says: Place the east-west length of 6 zhang, multiply it by the south-north length of 3 zhang, obtaining 1800 cubic chi.
Multiply this by 5, obtaining 9000.
Divide it by 2, and the result is the number of bricks.

Answer: *a* bricks.
"""

from fractions import Fraction

# Dimensions of the house foundation
南北 = 3  # in 丈
東西 = 6  # in 丈

# Conversion factor: 1 丈 = 10 尺
南北尺 = 南北 * 10
東西尺 = 東西 * 10

# Step 1: Calculate the total volume in cubic chi
體積 = 南北尺 * 東西尺  # 平方尺 (area)
體積 *= 1  # Assuming the height is 1 chi (not explicitly stated in the problem)

# Step 2: Multiply by 5 (bricks required for every 2 cubic chi)
磚需求 = 5 * 體積

# Step 3: Divide by 2 to account for the "2 cubic chi per 5 bricks" rule
a = Fraction(磚需求, 2)

# Output the result
a#----- content ends here -----

"""
"""
