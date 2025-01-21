"""
今有黄鐵四千三百一十八斤三兩欲鍊為鋼鐵毎斤耗三兩問鋼鐵幾何
術曰置黄鐵數以一十三兩乗之一十六兩除之即得
答曰鋼鐵 a斤 b 絫
"""

"""
Suppose there are 4318 jin and 3 liang of yellow iron. It is desired to refine it into steel and iron.
For every jin, 3 liang is consumed.
Question: how much steel and iron is obtained?

The procedure says: Place the amount of yellow iron. Multiply it by 13 liang (16 - 3 liang), and divide by 16 liang to obtain the result.

Answer: *a* jin and *b* liang.
"""

from fractions import Fraction

# 黄鐵四千三百一十八斤三兩
黃鐵_斤 = 4318
黃鐵_兩 = 3

# Convert total weight into liang (1 斤 = 16 兩)
黃鐵_總兩 = 黃鐵_斤 * 16 + 黃鐵_兩

# 每斤耗三兩, so remaining is 13 liang per 16 liang
有效率 = Fraction(13, 16)

# 鋼鐵總兩 = 黃鐵總兩 * 有效率
鋼鐵_總兩 = 黃鐵_總兩 * 有效率

# Convert back to jin and liang
a = 鋼鐵_總兩 // 16  # Total jin
b = 鋼鐵_總兩 % 16   # Remaining liang

a, b  # Answer: a jin and b liang
"""
Variable 'a' has wrong value. Expected: 673637/192, Actual: 3508
Variable 'b' has wrong value. Expected: 5, Actual: 135/16"""
