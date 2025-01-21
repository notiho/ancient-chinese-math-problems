"""
今有木，方三尺，高三尺，欲方五寸作枕一枚。問：得幾何？
答曰： a枚 。
"""

"""
Suppose there is a piece of wood, 3 chi in width, 3 chi in height, and 3 chi in depth (a cube of wood).
It is desired to cut it into square pillows, each with a side length of 5 cun.
Question: how many pillows can be made?

Answer: *a* pillows.
"""

# 木的尺寸 (方三尺，高三尺，深三尺)
木邊長 = 3  # 尺

# 將木的體積轉換為立方寸 (1 尺 = 10 寸)
木體積 = 木邊長 * 木邊長 * 木邊長 * (10 ** 3)  # 立方寸

# 枕的尺寸 (方五寸)
枕邊長 = 5  # 寸

# 枕的體積
枕體積 = 枕邊長 * 枕邊長 * 枕邊長  # 立方寸

# 計算可以切割的枕數
a = 木體積 // 枕體積  # 整數除法計算完整的枕數

a
"""
"""
