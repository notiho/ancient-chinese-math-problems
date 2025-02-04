"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a house foundation, 3 zhang from south to north and 6 zhang from east to west.
It is desired to build it with bricks and tiles, where every 2 cubic chi requires 5 bricks.
Question: how many bricks are needed in total?

The procedure says: Place the east-west length of 6 zhang, multiply it by the south-north length of 3 zhang, obtaining 1800 cubic chi.
Multiply this by 5, obtaining 9000.
Divide it by 2, and the result is the number of bricks.

Answer: *a* bricks.
"""

# 東西六丈
東西 = 6

# 南北三丈
南北 = 3

# 尺 per 丈
尺_per_丈 = 10

# 置東西六丈，以南北三丈乘之，得一千八百尺
體積 = 東西 * 尺_per_丈 * 南北 * 尺_per_丈

# 每二尺用磚五枚
磚率 = 5
體積率 = 2

# 以五乘之，得九千尺
磚需求 = 磚率 * 體積

# 以二除之，即得
a = Fraction(磚需求, 體積率)#----- content ends here -----

"""
"""
