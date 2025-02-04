"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a(=216)枚 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, 3 chi wide and 3 chi high, and it is desired to cut it into square blocks of 5 cun to make pillows.
Question: how many pillows can be made?

The procedure says: Place the 3 chi square, multiply it by itself, obtaining 9 chi.
Multiply it by the height of 3 chi, obtaining 27 chi.
Multiply it by 8 pillows per chi, and the result is obtained.

Answer: *a*(=216) pillows.
"""

# 木方三尺
方 = 3  # chi (width and height)

# 高三尺
高 = 3  # chi (height)

# 置方三尺，自相乘，得九尺
方積 = 方 * 方  # square area in chi^2

# 以高三尺乘之，得二十七尺
體積 = 方積 * 高  # volume in chi^3

# 以一尺木八枕乘之，即得
枕每尺 = 8  # 8 pillows per chi^3
a = 枕每尺 * 體積  # 216 pillows#----- content ends here -----

"""
"""
