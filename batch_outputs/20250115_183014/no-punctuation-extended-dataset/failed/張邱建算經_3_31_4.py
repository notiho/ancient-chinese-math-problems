"""
今有立方材三尺鋸為方枕一百二十五枚問一枚為立方幾何
術曰以材方寸數再自乘以枚數而一所得開立方除之得枕方
答曰 a枚 方 b寸
"""

"""
Suppose there is a cubic piece of wood with a side length of 3 chi. It is sawed into 125 rectangular blocks.
Question: how many cubic cun does each block have?

The procedure says: Take the cubic wood's side length in cun, square it, and multiply it by itself again (cube it). 
Multiply this by the number of blocks. Divide the result by 1.
Take the cube root of the result to find the volume of each block in cubic cun.

Answer: *a* blocks, each *b* cubic cun.
"""

# 立方材三尺
材邊長 = 3  # 尺

# 將邊長轉換為寸 (1 尺 = 10 寸)
材邊長寸 = 10 * 材邊長

# 鋸為方枕一百二十五枚
枕枚數 = 125

# 以材方寸數再自乘以枚數而一
材體積寸 = 材邊長寸 ** 3  # 材的立方體積 (寸^3)
總體積寸 = 材體積寸  # 總體積保持不變

# 所得開立方除之得枕方
枕方寸 = Fraction(總體積寸, 枕枚數)

a = 枕枚數
b = 枕方寸
"""
Variable 'a' has wrong value. Expected: 1, Actual: 125
Variable 'b' has wrong value. Expected: 6, Actual: 216"""
