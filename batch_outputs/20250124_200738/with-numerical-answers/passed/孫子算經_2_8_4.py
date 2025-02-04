"""
今有屋基，南北三丈，東西六丈，欲以磚瓦砌之，凡積二尺，用磚五枚。問：計幾何？
術曰：置東西六丈，以南北三丈乘之，得一千八百尺；以五乘之，得九千尺；以二除之，即得。
答曰： a(=4500)枚 。
"""

#----- content starts here -----
"""
Suppose there is a house foundation, 3 zhang from south to north and 6 zhang from east to west.
It is desired to build it with bricks and tiles, where every 2 cubic chi requires 5 bricks.
Question: how many bricks are needed?

The procedure says: Place the east-west length of 6 zhang, multiply it by the south-north length of 3 zhang, obtaining 1800 cubic chi.
Multiply this by 5, obtaining 9000.
Divide it by 2, and the result is obtained.

Answer: *a*(=4500) bricks.
"""

# 南北三丈
南北 = 3 * 10  # Convert zhang to chi

# 東西六丈
東西 = 6 * 10  # Convert zhang to chi

# 置東西六丈，以南北三丈乘之，得一千八百尺
積尺 = 東西 * 南北

# 每二尺用磚五枚
每二尺用磚 = 5

# 以五乘之，得九千尺
總磚需求 = 每二尺用磚 * 積尺

# 以二除之，即得
a = 總磚需求 // 2  # 4500 bricks#----- content ends here -----

"""
"""
