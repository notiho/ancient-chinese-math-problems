"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood, with a square cross-section of 3 chi by 3 chi, and a height of 3 chi.
It is desired to cut it into square pillows, each with a square cross-section of 5 cun by 5 cun and a height of 5 cun.
Question: how many pillows can be made?

Answer: *a* pillows.
"""

# 木的尺寸 (方三尺，高三尺)
木的邊長 = 3  # 尺
木的高度 = 3  # 尺

# 枕的尺寸 (方五寸，高五寸)
枕的邊長 = Fraction(5, 10)  # 尺 (5 寸 = 0.5 尺)
枕的高度 = Fraction(5, 10)  # 尺 (5 寸 = 0.5 尺)

# 計算木的體積
木的體積 = 木的邊長**2 * 木的高度  # 立方尺

# 計算每個枕的體積
枕的體積 = 枕的邊長**2 * 枕的高度  # 立方尺

# 計算可以切割的枕數
a = 木的體積 // 枕的體積  # 整數除法，表示完整的枕數

a#----- content ends here -----

"""
"""
