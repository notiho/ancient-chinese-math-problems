"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, 3 chi in width and 3 chi in height. It is desired to cut it into square blocks of 5 cun each to make pillows.
Question: how many pillows can be made?

The procedure says: Take the square width of 3 chi, multiply it by itself to get 9 square chi.
Then multiply it by the height of 3 chi to get 27 cubic chi.
For every 1 cubic chi of wood, 8 pillows can be made. Multiply this to get the result.

Answer: *a* pillows.
"""

from fractions import Fraction

# 木的尺寸
方 = 3  # 方三尺 (width)
高 = 3  # 高三尺 (height)

# 計算木的體積 (立方尺)
體積 = 方 * 方 * 高  # 自相乘得九尺，以高三尺乘之

# 每一立方尺木可製作 8 枕
每立方尺枕數 = 8

# 計算總枕數
a = 體積 * 每立方尺枕數

# 答案
a  # 枕的數量#----- content ends here -----

"""
"""
