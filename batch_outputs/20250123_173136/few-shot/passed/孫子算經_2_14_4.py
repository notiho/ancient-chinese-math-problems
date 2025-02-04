"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

"""
Suppose there is a piece of wood, 3 chi in width and 3 chi in height. It is desired to cut it into square blocks of 5 cun each to make pillows.
Question: how many pillows can be made?

The procedure says: Place the square width of 3 chi, multiply it by itself, obtaining 9 square chi.
Multiply this by the height of 3 chi, obtaining 27 cubic chi.
Multiply this by the number of pillows that can be made from 1 cubic chi of wood, which is 8, and the result is obtained.

Answer: *a* pillows.
"""

# 木方三尺
方 = 3  # chi

# 高三尺
高 = 3  # chi

# 置方三尺，自相乘，得九尺
方積 = 方 * 方  # square chi

# 以高三尺乘之，得二十七尺
體積 = 方積 * 高  # cubic chi

# 一尺木八枕
每尺枕數 = 8  # pillows per cubic chi

# 以一尺木八枕乘之，即得
a = 體積 * 每尺枕數  # total pillows
"""
"""
