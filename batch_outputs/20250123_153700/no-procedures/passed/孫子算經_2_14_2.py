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

# 木的尺寸 (立方體)
木_邊長 = 3  # 尺

# 將木的尺寸轉換為寸 (1 尺 = 10 寸)
木_邊長_寸 = 木_邊長 * 10  # 寸

# 木的體積 (立方寸)
木_體積 = 木_邊長_寸 ** 3  # 立方寸

# 每個枕的邊長
枕_邊長 = 5  # 寸

# 每個枕的體積 (立方寸)
枕_體積 = 枕_邊長 ** 3  # 立方寸

# 計算可以製作的枕數量
a = 木_體積 // 枕_體積  # 整數除法計算枕數量

a  # 答案: 可以製作的枕數量
"""
"""
