"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰一枚方 a寸
"""

"""
Suppose there is a cubic piece of wood with a side length of 3 chi. It is sawn into 125 rectangular blocks.
Question: how many cubic cun does each block have?

The procedure says: Take the number of cubic cun in the wood, square it, and multiply it by the number of blocks.
Take the cube root of the result, and divide it to obtain the volume of one block.

Answer: one block has *a* cubic cun.
"""

# 立方材三尺
材邊長 = 3  # 尺

# 轉換為寸 (1 尺 = 10 寸)
材邊長寸 = 材邊長 * 10

# 鋸為方枕一百二十五枚
枕枚數 = 125

# 以材方寸數再自乘
材方寸數 = 材邊長寸 ** 3

# 以枚數而一所得
總方寸數 = 材方寸數

# 除以枕枚數，得一枚方
a = Fraction(總方寸數, 枕枚數)
"""
Variable 'a' has wrong value. Expected: 6, Actual: 216"""
