"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a house foundation, 3 zhang from south to north, and 6 zhang from east to west.
It is desired to construct it with bricks and tiles, where every 2 cubic chi requires 5 bricks.
Question: how many bricks are needed?

The procedure says: Place the east-west length of 6 zhang, and multiply it by the south-north length of 3 zhang, obtaining 1800 square chi.
Multiply this by 5, obtaining 9000 cubic chi.
Divide this by 2, and the result is the number of bricks.

Answer: *a* bricks.
"""

# Dimensions of the house foundation
南北 = 3  # in 丈
東西 = 6  # in 丈

# Conversion: 1 丈 = 10 尺
南北 *= 10  # in 尺
東西 *= 10  # in 尺

# Step 1: Calculate the area of the foundation in square chi
面積 = 南北 * 東西  # in 平方尺

# Step 2: Multiply by 5 (bricks per 2 cubic chi)
積 = 面積 * 5  # in cubic 尺

# Step 3: Divide by 2 to calculate the number of bricks
a = Fraction(積, 2)

a#----- content ends here -----

"""
"""
