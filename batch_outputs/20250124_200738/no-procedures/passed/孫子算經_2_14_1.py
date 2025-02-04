"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
答曰： a枚 。
"""

#----- content starts here -----
"""
Suppose there is a piece of wood that is 3 chi wide, 3 chi long, and 3 chi high. 
It is desired to cut it into square blocks of 5 cun on each side to make pillows. 
Question: how many pillows can be made?

Answer: *a* pillows.
"""

# 木的尺寸 (3尺 x 3尺 x 3尺)
木_邊長 = 3  # 尺
木_體積 = 木_邊長 ** 3  # 體積 = 邊長的立方

# 枕的尺寸 (5寸 x 5寸 x 5寸)
枕_邊長 = Fraction(5, 10)  # 5寸 = 0.5尺
枕_體積 = 枕_邊長 ** 3  # 體積 = 邊長的立方

# 計算可切割的枕數量
a = 木_體積 // 枕_體積  # 整數除法計算枕的數量

a#----- content ends here -----

"""
"""
