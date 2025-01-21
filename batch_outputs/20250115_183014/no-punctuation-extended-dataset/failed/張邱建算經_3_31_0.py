"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰 a枚 方 b寸
"""

"""
Suppose there is a cubic piece of wood with a side length of 3 chi. It is sawed into 125 rectangular blocks.
Question: how many cubic cun does each block have?

The procedure says: Take the number of cubic cun in the original wood, square it, and multiply it by the number of blocks.
Take the result, extract the cube root, and divide it to obtain the volume of each block.

Answer: *a* blocks, each *b* cubic cun.
"""

from fractions import Fraction

# 立方材三尺
材邊長 = 3  # 尺

# 轉換為寸 (1 尺 = 10 寸)
材邊長寸 = 材邊長 * 10  # 寸

# 計算材的立方寸數
材立方寸數 = 材邊長寸 ** 3  # 立方寸

# 鋸為方枕一百二十五枚
枕數 = 125

# 每枚的立方寸數
每枚立方寸數 = Fraction(材立方寸數, 枕數)

# 答案
a = 枕數
b = 每枚立方寸數
"""
Variable 'a' has wrong value. Expected: 1, Actual: 125
Variable 'b' has wrong value. Expected: 6, Actual: 216"""
