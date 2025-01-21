"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰 a枚 方 b寸
"""

"""
Suppose there is a cubic block of wood with a side length of 3 chi. It is sawed into 125 rectangular beams.
Question: how many cubic cun does each beam have?

The procedure says: Take the number of cubic cun in the block, square it, and multiply it by the number of beams.
Take the cube root of the result and divide it, obtaining the volume of each beam.

Answer: *a* beams, each *b* cubic cun.
"""

from fractions import Fraction

# 立方材三尺
材邊長 = 3  # 尺

# 轉換為寸 (1 尺 = 10 寸)
材邊長寸 = 材邊長 * 10

# 鋸為方枕一百二十五枚
枕枚數 = 125

# 材方寸數再自乘
材方寸數 = 材邊長寸 ** 3  # 立方寸數

# 以枚數而一所得
總立方寸 = 材方寸數

# 每枚的立方寸數
每枚立方寸 = Fraction(總立方寸, 枕枚數)

# 答案
a = 枕枚數
b = 每枚立方寸
"""
Variable 'a' has wrong value. Expected: 1, Actual: 125
Variable 'b' has wrong value. Expected: 6, Actual: 216"""
