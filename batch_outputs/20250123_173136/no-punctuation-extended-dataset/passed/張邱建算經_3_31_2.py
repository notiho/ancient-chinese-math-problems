"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰一枚方 a寸
"""

"""
Suppose there is a cubic block of wood with a side length of 3 chi. It is sawn into 125 rectangular blocks.
Question: how many cubic cun does one block have?

The procedure says: Take the number of cubic cun in the wood, square it again, and multiply by the number of blocks.
Take the cube root of the result, and divide it to obtain the volume of one block.

Answer: one block has *a* cubic cun.
"""

# 立方材三尺
材邊長 = 3  # 尺

# 轉換為寸 (1 尺 = 10 寸)
材邊長寸 = 10 * 材邊長

# 計算材的方寸數 (立方)
材方寸數 = 材邊長寸 ** 3

# 方枕一百二十五枚
枚數 = 125

# 以材方寸數再自乘
再自乘 = 材方寸數

# 以枚數而一所得
所得 = 再自乘 / 枚數

# 開立方
枕方 = 所得 ** (1 / 3)

a = Fraction(枕方).limit_denominator(1000)  # Approximation for clarity
"""
"""
