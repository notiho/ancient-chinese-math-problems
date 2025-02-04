"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, 3 chi wide and 3 chi tall, and it is desired to cut it into square blocks of 5 cun (as pillows).
Question: how many blocks can be obtained?

The procedure says: Place the square width of 3 chi, multiply it by itself, obtaining 9 square chi.
Multiply this by the height of 3 chi, obtaining 27 cubic chi.
Multiply this by the fact that 1 cubic chi of wood can make 8 blocks, and the result is obtained.

Answer: *a* blocks.
"""

from fractions import Fraction

# 木的尺寸
方 = 3  # 方三尺 (width)
高 = 3  # 高三尺 (height)

# 計算木的體積（立方尺）
體積 = 方 * 方 * 高  # 自相乘得九尺，再乘高三尺

# 每立方尺木可製作 8 枕
每立方尺枕數 = 8

# 計算總枕數
a = 體積 * 每立方尺枕數

# 答案
a#----- content ends here -----

"""
"""
