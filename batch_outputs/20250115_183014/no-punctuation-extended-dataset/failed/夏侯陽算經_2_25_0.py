"""
今有黄鐵四千三百一十八斤三兩欲鍊為鋼鐵毎斤耗三兩問鋼鐵幾何
術曰置黄鐵數以一十三兩乗之一十六兩除之即得
答曰鋼鐵 a斤 b 絫
"""

"""
Suppose there are 4318 jin and 3 liang of yellow iron. It is desired to refine it into steel, where each jin loses 3 liang.
Question: how much steel is obtained?

The procedure says: Place the amount of yellow iron. Multiply it by 13 liang (the remaining weight after losing 3 liang per jin). Divide it by 16 liang (to convert back to jin). The result is the amount of steel.

Answer: *a* jin and *b* liang.
"""

# 黄鐵四千三百一十八斤三兩
黃鐵_斤 = 4318
黃鐵_兩 = 3

# Convert all to liang (1 jin = 16 liang)
黃鐵_總兩 = 黃鐵_斤 * 16 + 黃鐵_兩

# 每斤耗三兩, so remaining weight per jin is 13 liang
剩餘每斤 = 13

# Multiply by 13 liang
鋼鐵_總兩 = 黃鐵_總兩 * 剩餘每斤

# Divide by 16 liang to convert back to jin
鋼鐵_斤 = 鋼鐵_總兩 // 16
鋼鐵_兩 = 鋼鐵_總兩 % 16

a = 鋼鐵_斤
b = 鋼鐵_兩
"""
Variable 'a' has wrong value. Expected: 673637/192, Actual: 56136
Variable 'b' has wrong value. Expected: 5, Actual: 7"""
