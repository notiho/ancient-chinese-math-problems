"""
今有木方三尺高三尺欲方五寸作枕一枚問得幾何
術曰置方三尺自相乘得九尺以高三尺乘之得二十七尺以一尺木八枕乘之即得
答曰 a枚 
"""

#----- content starts here -----
"""
Suppose there is a cubic piece of wood with a square base of 3 chi by 3 chi and a height of 3 chi.
It is desired to cut it into square wooden blocks with a side length of 5 cun to make pillows.
Question: how many pillows can be made?

The procedure says: Place the square base of 3 chi, multiply it by itself, obtaining 9 square chi.
Multiply this by the height of 3 chi, obtaining 27 cubic chi.
Multiply 1 cubic chi by 8 pillows, then divide the total volume by this value to obtain the number of pillows.

Answer: *a* pillows.
"""

# 木方三尺
方長 = 3  # chi
方寬 = 3  # chi
方高 = 3  # chi

# 方三尺，自相乘，得九尺
方面積 = 方長 * 方寬  # square chi

# 以高三尺乘之，得二十七尺
方體積 = 方面積 * 方高  # cubic chi

# 以一尺木八枕乘之
一尺木枕數 = 8  # 1 cubic chi makes 8 pillows

# 即得
a = 方體積 * 一尺木枕數  # total number of pillows#----- content ends here -----

"""
"""
