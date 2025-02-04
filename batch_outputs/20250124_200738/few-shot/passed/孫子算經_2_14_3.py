"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, 3 chi square in cross-section and 3 chi in height. 
It is desired to cut it into pillows, each 5 cun square in cross-section.
Question: how many pillows can be made?

The procedure says: Place the 3 chi square cross-section, multiply it by itself, obtaining 9 chi.
Multiply this by the height of 3 chi, obtaining 27 chi.
Multiply this by the fact that 1 chi of wood makes 8 pillows, and the result is obtained.

Answer: *a* pillows.
"""

# 木方三尺
方 = 3

# 高三尺
高 = 3

# 置方三尺，自相乘，得九尺
橫截面積 = 方 * 方

# 以高三尺乘之，得二十七尺
體積 = 橫截面積 * 高

# 一尺木八枕
每尺枕數 = 8

# 以一尺木八枕乘之，即得
a = 體積 * 每尺枕數#----- content ends here -----

"""
"""
