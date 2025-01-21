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

Answer: *a* jin and *b* liang.
"""

from fractions import Fraction

# 黄鐵數
黃鐵_斤 = 4318
黃鐵_絫 = 3

# Convert 黄鐵 to total 絫 (1 斤 = 16 絫)
黃鐵_總絫 = 黃鐵_斤 * 16 + 黃鐵_絫

# 每斤耗三兩 -> 每斤剩十三兩
鋼鐵率 = 13  # 剩下的絫數

# 以一十三兩乘之
鋼鐵_總絫 = 黃鐵_總絫 * 鋼鐵率

# 一十六兩除之
鋼鐵_總絫 = Fraction(鋼鐵_總絫, 16)

# Convert total 絫 back to 斤 and 絫
a = 鋼鐵_總絫 // 16  # 斤
b = 鋼鐵_總絫 % 16  # 絫
"""
Variable 'a' has wrong value. Expected: 673637/192, Actual: 3508
Variable 'b' has wrong value. Expected: 5, Actual: 135/16"""
