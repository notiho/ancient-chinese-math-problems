"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰 a枚 方 b寸
"""

"""
Suppose there is a cubic block of wood with a side length of 3 chi. It is sawn into 125 rectangular blocks.
Question: how many cubic cun does each block have?

The procedure says: Take the number of cubic cun in the block, square it again, and multiply it by the number of blocks.
Take the cube root of the result, and divide it, obtaining the volume of each block.

Answer: *a* blocks, each *b* cubic cun.
"""

from fractions import Fraction

# 立方材三尺
材邊長 = 3  # 尺

# 轉換為寸 (1 尺 = 10 寸)
材邊長寸 = 10 * 材邊長

# 材方寸數
材方寸數 = 材邊長寸 ** 3

# 方枕一百二十五枚
枚數 = 125

# 以材方寸數再自乘
材方寸數平方 = 材方寸數 ** 2

# 以枚數而一所得
積 = 材方寸數平方 * 枚數

# 開立方
枕方寸數 = round(積 ** (1 / 3))

# 每一枚的立方寸數
b = Fraction(枕方寸數)

a = 枕方寸數
"""
Variable 'a' has wrong value. Expected: 1, Actual: 4500
Variable 'b' has wrong value. Expected: 6, Actual: 4500"""
