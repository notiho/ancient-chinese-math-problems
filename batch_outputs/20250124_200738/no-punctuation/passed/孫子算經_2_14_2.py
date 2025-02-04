"""
今有木方三尺高三尺欲方五寸作枕一枚問得幾何
術曰置方三尺自相乘得九尺以高三尺乘之得二十七尺以一尺木八枕乘之即得
答曰 a枚 
"""

#----- content starts here -----
"""
Suppose there is a wooden block with a square base of 3 chi by 3 chi and a height of 3 chi.
It is desired to cut it into square wooden pillows, each with a square base of 5 cun by 5 cun and a height of 5 cun.
Question: how many pillows can be made?

The procedure says: Place the square base of 3 chi, multiply it by itself, obtaining 9 square chi.
Multiply it by the height of 3 chi, obtaining 27 cubic chi.
For each cubic chi of wood, 8 pillows can be made.
Multiply by 8, and the result is obtained.

The answer says: *a* pillows.
"""

# 木方三尺
木方邊長 = 3  # chi
木方高 = 3  # chi

# 方三尺，自相乘，得九尺
木方底面積 = 木方邊長 * 木方邊長  # square chi

# 以高三尺乘之，得二十七尺
木方體積 = 木方底面積 * 木方高  # cubic chi

# 一尺木八枕
每立方尺枕數 = 8

# 乘之，即得
a = 木方體積 * 每立方尺枕數  # 枕數 (number of pillows)#----- content ends here -----

"""
"""
