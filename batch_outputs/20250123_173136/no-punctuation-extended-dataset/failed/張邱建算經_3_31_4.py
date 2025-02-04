"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰一枚方 a寸
"""

"""
Suppose there is a cubic piece of wood with a side length of 3 chi. It is sawed into 125 rectangular blocks.
Question: how many cubic cun does each block have?

The procedure says: Take the cubic wood's side length in cun, square it, and multiply it by itself again (cube it). 
Multiply this by the number of blocks. Divide the result by the number of blocks, and take the cube root of the result.
This gives the cubic cun of each block.

Answer: each block is *a* cubic cun.
"""

# 立方材三尺
材邊長 = 3  # 尺

# Convert to 寸 (1 尺 = 10 寸)
材邊長寸 = 材邊長 * 10

# 鋸為方枕一百二十五枚
枚數 = 125

# 以材方寸數再自乘以枚數而一所得
材體積 = 材邊長寸 ** 3  # 材的立方體積 (立方寸)

# 每枚的體積
每枚體積 = Fraction(材體積, 枚數)

# 一枚為立方幾何
a = 每枚體積
"""
Variable 'a' has wrong value. Expected: 6, Actual: 216"""
