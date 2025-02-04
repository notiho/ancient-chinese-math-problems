"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

"""
Suppose there is a piece of wood, 3 chi square in cross-section and 3 chi in height.
It is desired to cut it into pillows, each 5 cun square in cross-section.
Question: how many pillows can be obtained?

The procedure says: Place the 3 chi square cross-section, multiply it by itself, obtaining 9 chi.
Multiply this by the height of 3 chi, obtaining 27 chi.
Multiply this by the fact that 1 chi of wood makes 8 pillows, and the result is obtained.

Answer: *a* pillows.
"""

from fractions import Fraction

# 木方三尺
方 = 3

# 高三尺
高 = 3

# 置方三尺，自相乘，得九尺
方積 = 方 * 方

# 以高三尺乘之，得二十七尺
體積 = 方積 * 高

# 一尺木八枕
枕率 = 8

# 以一尺木八枕乘之，即得
a = 枕率 * 體積
"""
"""
