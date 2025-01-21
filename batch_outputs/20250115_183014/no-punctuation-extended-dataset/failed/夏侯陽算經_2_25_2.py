"""
今有黄鐵四千三百一十八斤三兩欲鍊為鋼鐵毎斤耗三兩問鋼鐵幾何
術曰置黄鐵數以一十三兩乗之一十六兩除之即得
答曰鋼鐵 a斤 b 絫
"""

"""
Suppose there are 4318 jin and 3 liang of yellow iron. It is desired to refine it into steel.
For every jin, 3 liang are lost.
Question: how much steel is obtained?

The procedure says: Place the amount of yellow iron.
Multiply it by 13 liang (16 liang - 3 liang).
Divide it by 16 liang.
This gives the result.

Answer: *a* jin and *b* liang of steel.
"""

from fractions import Fraction

# 黄鐵四千三百一十八斤三兩
黃鐵_斤 = 4318
黃鐵_兩 = 3

# Convert all to liang (1 斤 = 16 兩)
黃鐵_總兩 = 黃鐵_斤 * 16 + 黃鐵_兩

# 每斤耗三兩 (thus, 1 jin becomes 13 liang of steel)
鋼鐵_每斤_兩 = 16 - 3

# 以一十三兩乘之
鋼鐵_總兩 = 黃鐵_總兩 * 鋼鐵_每斤_兩

# 一十六兩除之
鋼鐵_總兩 = Fraction(鋼鐵_總兩, 16)

# Convert back to jin and liang
a = 鋼鐵_總兩 // 16  # Whole jin
b = 鋼鐵_總兩 % 16   # Remaining liang

a, b  # Answer in jin and liang
"""
Variable 'a' has wrong value. Expected: 673637/192, Actual: 3508
Variable 'b' has wrong value. Expected: 5, Actual: 135/16"""
