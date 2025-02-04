"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰一枚方 a寸
"""

"""
Suppose there is a cubic block of wood with a side length of 3 chi. It is sawed into 125 rectangular blocks.
Question: how many cubic cun does each block have?

The procedure says: Take the number of cubic cun in the wood, square it again, and multiply it by the number of blocks.
Take the result, extract the cube root, and divide it, obtaining the volume of each block.

Answer: each block has *a* cubic cun.
"""

from fractions import Fraction

# 立方材三尺
材邊長 = 3  # in chi

# Convert chi to cun (1 chi = 10 cun)
材邊長_cun = 10 * 材邊長

# Compute the total cubic cun of the wood
材方寸數 = 材邊長_cun ** 3

# 鋸為方枕一百二十五枚
枚數 = 125

# 以材方寸數再自乘
材方寸數平方 = 材方寸數 ** 2

# 以枚數而一
總積 = 材方寸數平方 * 枚數

# 所得開立方
每枚方寸數 = Fraction(材方寸數, 枚數)

# 答曰一枚方 a寸
a = 每枚方寸數
"""
Variable 'a' has wrong value. Expected: 6, Actual: 216"""
