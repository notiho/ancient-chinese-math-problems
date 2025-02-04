"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰一枚方 a寸
"""

"""
Suppose there is a cubic block of wood with a side length of 3 chi. It is sawed into 125 rectangular blocks.
Question: how many cubic cun does each block have?

The procedure says: Take the number of cubic cun in the block, square it, and multiply it by the number of blocks.
Take the result and extract the cube root, dividing it to obtain the volume of each block.

Answer: each block has *a* cubic cun.
"""

# 立方材三尺
材邊長 = 3  # 尺

# 轉換為寸 (1 尺 = 10 寸)
材邊長寸 = 材邊長 * 10

# 材方寸數再自乘
材方寸數 = 材邊長寸 ** 3  # 立方材的體積 (立方寸)

# 方枕一百二十五枚
枚數 = 125

# 以材方寸數再自乘以枚數而一
總體積 = 材方寸數

# 所得開立方除之得枕方
a = Fraction(總體積, 枚數)  # 每枚的體積 (立方寸)
"""
Variable 'a' has wrong value. Expected: 6, Actual: 216"""
