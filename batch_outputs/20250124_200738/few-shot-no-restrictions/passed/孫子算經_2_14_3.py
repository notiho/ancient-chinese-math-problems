"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
術曰：置方三尺，自相乘，得九尺，以高三尺乘之，得二十七尺，以一尺木八枕乘之，即得。
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, 3 chi in width and 3 chi in height. It is desired to cut it into square blocks of 5 cun (as pillows).
Question: how many blocks can be obtained?

The procedure says: Place the square width of 3 chi, multiply it by itself, obtaining 9 square chi.
Multiply this by the height of 3 chi, obtaining 27 cubic chi.
Multiply this by the number of pillows that can be made from 1 cubic chi (8 pillows per cubic chi), and the result is obtained.

Answer: *a* blocks.
"""

# 木的方三尺
方 = 3  # 方形的邊長 (chi)

# 高三尺
高 = 3  # 高度 (chi)

# 方三尺，自相乘，得九尺
方積 = 方 * 方  # 面積 (平方尺)

# 以高三尺乘之，得二十七尺
體積 = 方積 * 高  # 體積 (立方尺)

# 一尺木八枕
枕率 = 8  # 每立方尺可製作的枕數

# 以一尺木八枕乘之，即得
a = 枕率 * 體積  # 總枕數

a  # 答案#----- content ends here -----

"""
"""
