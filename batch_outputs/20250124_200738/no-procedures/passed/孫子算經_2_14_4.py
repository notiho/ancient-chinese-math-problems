"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a block of wood, 3 chi in width, 3 chi in height, and 3 chi in depth. 
It is desired to cut it into square pillows, each with a side length of 5 cun. 
Question: how many pillows can be made?

Answer: *a* pillows.
"""

# 木的尺寸 (方三尺，高三尺)
木_邊長 = 3  # 尺
木_體積 = 木_邊長 ** 3  # 體積 = 邊長的立方

# 每個枕的尺寸 (方五寸)
枕_邊長 = Fraction(5, 10)  # 5 寸 = 0.5 尺
枕_體積 = 枕_邊長 ** 3  # 體積 = 邊長的立方

# 計算可以切割的枕數
a = 木_體積 // 枕_體積  # 使用整數除法，因為只能切割完整的枕

a#----- content ends here -----

"""
"""
