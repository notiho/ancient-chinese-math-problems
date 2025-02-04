"""
今有屋基南北三丈東西六丈欲以磚瓦砌之凡積二尺用磚五枚問計幾何
術曰置東西六丈以南北三丈乘之得一千八百尺以五乘之得九千尺以二除之即得
答曰 a枚 
"""

"""
Suppose there is a house foundation with a north-south length of 3 zhang and an east-west length of 6 zhang.
It is desired to build it with bricks and tiles, where every 2 cubic chi requires 5 bricks.
Question: how many bricks are needed in total?

The procedure says: Place the east-west length of 6 zhang, multiply it by the north-south length of 3 zhang, obtaining 1800 cubic chi.
Multiply it by 5, obtaining 9000.
Divide it by 2, and the result is obtained.

Answer: *a* bricks.
"""

# 東西六丈
東西 = 6

# 南北三丈
南北 = 3

# 每積二尺用磚五枚
每二尺用磚 = 5
積單位 = 2

# 置東西六丈，以南北三丈乘之，得一千八百尺
積尺 = 東西 * 南北 * 100  # Convert zhang to chi (1 zhang = 10 chi)

# 以五乘之，得九千尺
總磚需求 = 每二尺用磚 * 積尺

# 以二除之，即得
a = 總磚需求 // 積單位
"""
"""
