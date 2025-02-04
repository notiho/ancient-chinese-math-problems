"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, 3 chi square in cross-section and 3 chi tall.
It is desired to cut it into pillows, each 5 cun square in cross-section.
Question: how many pillows can be made?

The procedure says: Place the 3 chi square cross-section, multiply it by itself, obtaining 9 square chi.
Multiply this by the height of 3 chi, obtaining 27 cubic chi.
Multiply this by the fact that 1 cubic chi of wood makes 8 pillows, and the result is obtained.

Answer: *a* pillows.
"""

from fractions import Fraction

# 木的尺寸
方 = 3  # 方形的邊長（尺）
高 = 3  # 高度（尺）

# 每一尺木可製作的枕數
每尺木枕數 = 8

# 計算木的體積（立方尺）
體積 = 方 * 方 * 高  # 方形截面積乘以高度

# 計算可製作的枕數
a = 體積 * 每尺木枕數

a  # 答案是 a 枚#----- content ends here -----

"""
"""
