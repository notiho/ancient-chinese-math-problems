"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

"""
Suppose there is a piece of wood, 3 chi wide and 3 chi high, and it is desired to cut it into pillow blocks, each 5 cun wide.
Question: how many pillow blocks can be obtained?

The procedure says: Place the 3 chi width, multiply it by itself, obtaining 9 square chi.
Multiply this by the 3 chi height, obtaining 27 cubic chi.
Multiply this by the fact that 1 cubic chi of wood makes 8 pillow blocks, and the result is obtained.

Answer: *a* blocks.
"""

# 木方三尺
方 = 3  # chi (width)

# 高三尺
高 = 3  # chi (height)

# 置方三尺，自相乘，得九尺
方積 = 方 * 方  # square chi

# 以高三尺乘之，得二十七尺
體積 = 方積 * 高  # cubic chi

# 一尺木八枕
枕率 = 8  # blocks per cubic chi

# 以一尺木八枕乘之，即得
a = 枕率 * 體積  # total blocks
"""
"""
