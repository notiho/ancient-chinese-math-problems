"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a(=216)枚 。
"""

"""
Suppose there is a piece of wood, 3 chi in width and 3 chi in height. It is desired to cut it into square blocks of 5 cun to make one pillow each.
Question: how many pillows can be made?

The procedure says: Place the 3 chi width, multiply it by itself, obtaining 9 chi². Multiply this by the 3 chi height, obtaining 27 chi³.
Multiply this by the fact that 1 chi³ of wood makes 8 pillows, and the result is obtained.

Answer: *a*(=216) pillows.
"""

# 木方三尺
方 = 3  # chi (width and height)

# 高三尺
高 = 3  # chi (length)

# 置方三尺，自相乘，得九尺
橫截面積 = 方 * 方  # 3 * 3 = 9 chi²

# 以高三尺乘之，得二十七尺
體積 = 橫截面積 * 高  # 9 * 3 = 27 chi³

# 一尺木八枕
枕率 = 8  # 1 chi³ makes 8 pillows

# 以一尺木八枕乘之，即得
a = 體積 * 枕率  # 27 * 8 = 216 pillows
"""
"""
