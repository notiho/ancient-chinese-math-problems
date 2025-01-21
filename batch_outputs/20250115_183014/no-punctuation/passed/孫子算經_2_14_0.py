"""
今有木方三尺高三尺欲方五寸作枕一枚問得幾何
術曰置方三尺自相乘得九尺以高三尺乘之得二十七尺以一尺木八枕乘之即得
答曰 a枚 
"""

"""
Suppose there is a cubic piece of wood with a width of 3 chi and a height of 3 chi.
It is desired to cut it into square wooden pillows, each with a side length of 5 cun.
Question: how many pillows can be obtained?

The procedure says: Place the square width of 3 chi, multiply it by itself, obtaining 9 square chi.
Multiply this by the height of 3 chi, obtaining 27 cubic chi.
For each 1 cubic chi of wood, 8 pillows can be made.
Multiply by 8 to obtain the result.

The answer says: *a* pillows.
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
每尺枕數 = 8

# 乘之，即得
a = 體積 * 每尺枕數  # 枕數 (number of pillows)
"""
"""
