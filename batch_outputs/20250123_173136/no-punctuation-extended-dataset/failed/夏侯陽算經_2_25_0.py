"""
今有黄鐵四千三百一十八斤三兩欲鍊為鋼鐵毎斤耗三兩問鋼鐵幾何
術曰置黄鐵數以一十三兩乗之一十六兩除之即得
答曰鋼鐵 a斤
"""

"""
Suppose there are 4318 jin and 3 liang of yellow iron. It is desired to refine it into steel and iron.
For every jin, 3 liang are lost.
Question: how much steel and iron is obtained?

The procedure says: Place the amount of yellow iron.
Multiply it by 13 liang (1 jin minus 3 liang), and divide it by 16 liang (1 jin).
This gives the result.

Answer: it makes *a* jin of steel and iron.
"""

from fractions import Fraction

# 黄鐵四千三百一十八斤三兩
黃鐵_斤 = 4318
黃鐵_兩 = 3

# Convert total weight to liang (1 斤 = 16 兩)
黃鐵_總兩 = 黃鐵_斤 * 16 + 黃鐵_兩

# 每斤耗三兩, so 1 斤 becomes 13 兩
有效_每斤 = 13

# 以一十三兩乘之
有效_總兩 = 有效_每斤 * 黃鐵_總兩

# 一十六兩除之
鋼鐵_總斤 = Fraction(有效_總兩, 16)

a = 鋼鐵_總斤
"""
Variable 'a' has wrong value. Expected: 898183/256, Actual: 898183/16"""
