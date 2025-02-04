"""
今有木方三尺高三尺欲方五寸作枕一枚問得幾何
術曰置方三尺自相乘得九尺以高三尺乘之得二十七尺以一尺木八枕乘之即得
答曰 a枚 
"""

#----- content starts here -----
"""
Suppose there is a cubic piece of wood with a square base of 3 chi and a height of 3 chi.
It is desired to cut it into square wooden blocks with a side length of 5 cun to make pillow blocks.
Question: how many pillow blocks can be made?

The procedure says: Place the square base of 3 chi, multiply it by itself, obtaining 9 square chi.
Multiply it by the height of 3 chi, obtaining 27 cubic chi.
For each cubic chi of wood, 8 pillow blocks can be made.
Multiply the total cubic chi by 8, and the result is the number of pillow blocks.

The answer says: *a* pillow blocks.
"""

# 木方三尺
方 = 3  # chi

# 高三尺
高 = 3  # chi

# 置方三尺，自相乘，得九尺
底面積 = 方 * 方  # square chi

# 以高三尺乘之，得二十七尺
體積 = 底面積 * 高  # cubic chi

# 以一尺木八枕乘之，即得
枕率 = 8  # 1 cubic chi produces 8 pillow blocks
a = 枕率 * 體積  # total number of pillow blocks#----- content ends here -----

"""
"""
