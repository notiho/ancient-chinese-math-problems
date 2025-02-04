"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, 3 chi wide and 3 chi tall. It is desired to cut it into square blocks of 5 cun (as pillows).
Question: how many blocks can be made?

The procedure says: Take the square width of 3 chi, multiply it by itself, obtaining 9 square chi.
Then multiply it by the height of 3 chi, obtaining 27 cubic chi.
Multiply this by the fact that 1 cubic chi of wood makes 8 blocks, and the result is obtained.

Answer: *a* blocks.
"""

from fractions import Fraction

# 木的尺寸
方 = 3  # 方三尺 (width)
高 = 3  # 高三尺 (height)

# 方三尺，自相乘，得九尺
方積 = 方 * 方  # 3 * 3 = 9 平方尺

# 以高三尺乘之，得二十七尺
體積 = 方積 * 高  # 9 * 3 = 27 立方尺

# 一尺木八枕
枕率 = 8  # 每立方尺木可製作 8 枕

# 以一尺木八枕乘之，即得
a = 枕率 * 體積  # 8 * 27 = 216 枕

a  # 答案是 216 枚枕#----- content ends here -----

"""
"""
