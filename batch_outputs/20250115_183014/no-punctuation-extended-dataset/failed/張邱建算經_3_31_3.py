"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰 a枚 方 b寸
"""

"""
Suppose there is a cubic block of wood with a side length of 3 chi. It is sawn into 125 rectangular blocks.
Question: how many cubic cun does each block have?

The procedure says: Take the cubic block's side length in cun, square it, and multiply it by itself again (i.e., cube it).
Then multiply by the number of blocks.
Divide the result by the number of blocks, and take the cube root of the result to find the side length of each block in cun.

Answer: *a* blocks, each with a side length of *b* cun.
"""

from fractions import Fraction

# 立方材三尺
材邊長 = 3  # in chi

# Convert to cun (1 chi = 10 cun)
材邊長_cun = 10 * 材邊長

# 鋸為方枕一百二十五枚
枕枚數 = 125

# 以材方寸數再自乘以枚數而一所得
材體積_cun = 材邊長_cun ** 3  # Cube the side length to get the volume in cubic cun
每枕體積_cun = Fraction(材體積_cun, 枕枚數)  # Divide the total volume by the number of blocks

# 開立方除之得枕方
枕邊長_cun = 每枕體積_cun ** Fraction(1, 3)  # Take the cube root to find the side length of each block

a = 枕枚數
b = 枕邊長_cun
"""
Variable 'a' has wrong value. Expected: 1, Actual: 125
Variable 'b' has wrong value. Expected: 6, Actual: 5.999999999999999"""
