"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a(=216)枚 。
"""

"""
Suppose there is a piece of wood, 3 chi in width and 3 chi in height, and it is desired to cut it into square blocks of 5 cun to make pillows.
Question: how many pillows can be made?

The procedure says: Place the width of 3 chi, multiply it by itself, obtaining 9 chi².
Multiply this by the height of 3 chi, obtaining 27 chi³.
Multiply this by the fact that 1 chi³ of wood makes 8 pillows, and the result is obtained.

Answer: *a*(=216) pillows.
"""

# 木方三尺
方 = 3  # chi

# 高三尺
高 = 3  # chi

# 置方三尺，自相乘，得九尺
橫截面積 = 方 * 方  # chi²

# 以高三尺乘之，得二十七尺
體積 = 橫截面積 * 高  # chi³

# 一尺木八枕
每尺枕數 = 8

# 以一尺木八枕乘之，即得
a = 體積 * 每尺枕數  # 216 pillows
"""
"""
