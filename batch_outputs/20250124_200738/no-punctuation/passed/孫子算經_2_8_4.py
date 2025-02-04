"""
今有屋基南北三丈東西六丈欲以磚瓦砌之凡積二尺用磚五枚問計幾何
術曰置東西六丈以南北三丈乘之得一千八百尺以五乘之得九千尺以二除之即得
答曰 a枚 
"""

#----- content starts here -----
"""
Suppose there is a house foundation with a north-south length of 3 zhang and an east-west length of 6 zhang.
It is desired to build it with bricks and tiles, with a total volume of 2 chi requiring 5 bricks.
Question: how many bricks are needed in total?

The procedure says: Place the east-west length of 6 zhang and multiply it by the north-south length of 3 zhang, obtaining 1800 chi.
Multiply this by 5, obtaining 9000 chi.
Divide it by 2, and the result is the number of bricks.

Answer: *a* bricks.
"""

# 東西六丈
東西 = 6

# 南北三丈
南北 = 3

# 置東西六丈以南北三丈乘之，得一千八百尺
積尺 = 東西 * 南北 * 100  # 1丈 = 10尺, so convert to chi

# 以五乘之，得九千尺
積磚 = 5 * 積尺

# 以二除之，即得
a = Fraction(積磚, 2)  # Total number of bricks#----- content ends here -----

"""
"""
