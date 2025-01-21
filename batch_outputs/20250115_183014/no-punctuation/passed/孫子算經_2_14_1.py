"""
今有木方三尺高三尺欲方五寸作枕一枚問得幾何
術曰置方三尺自相乘得九尺以高三尺乘之得二十七尺以一尺木八枕乘之即得
答曰 a枚 
"""

"""
Suppose there is a cubic piece of wood with a length of 3 chi, a width of 3 chi, and a height of 3 chi.
It is desired to cut it into square beams of 5 cun (0.5 chi) on each side, to make pillow blocks.
Question: how many pillow blocks can be made?

The procedure says: Place the square side of 3 chi, multiply it by itself, obtaining 9 chi².
Multiply this by the height of 3 chi, obtaining 27 chi³.
For each 1 chi³ of wood, 8 pillow blocks can be made.
Multiply by 8, and the result is obtained.

The answer says: *a* pillow blocks.
"""

# 木方三尺
木方邊長 = 3  # chi

# 置方三尺，自相乘，得九尺
木方面積 = 木方邊長 * 木方邊長  # chi²

# 以高三尺乘之，得二十七尺
木方體積 = 木方面積 * 木方邊長  # chi³

# 以一尺木八枕乘之，即得
枕每立方尺 = 8
a = 木方體積 * 枕每立方尺  # 枕數

a
"""
"""
