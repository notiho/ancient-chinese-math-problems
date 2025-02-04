"""
今有黄鐵四千三百一十八斤三兩欲鍊為鋼鐵毎斤耗三兩問鋼鐵幾何
術曰置黄鐵數以一十三兩乗之一十六兩除之即得
答曰鋼鐵 a斤
"""

#----- content starts here -----
"""
Suppose there are 4318 jin and 3 liang of yellow iron. It is desired to refine it into steel and iron.
For every jin, 3 liang are lost.
Question: how much steel and iron is obtained?

The procedure says: Place the amount of yellow iron.
Multiply it by 13 liang (the remaining part after 3 liang loss).
Divide it by 16 liang (to convert back to jin).
This gives the result.

Answer: it makes *a* jin of steel and iron.
"""

# 黄鐵四千三百一十八斤三兩
黃鐵_斤 = 4318
黃鐵_兩 = 3

# Convert total weight to liang (1 斤 = 16 兩)
黃鐵_總兩 = 黃鐵_斤 * 16 + 黃鐵_兩

# 每斤耗三兩, so 13 liang remains per 16 liang
剩餘率 = 13

# 以一十三兩乘之
鋼鐵_總兩 = 黃鐵_總兩 * 剩餘率

# 一十六兩除之 (convert back to jin)
a = Fraction(鋼鐵_總兩, 16)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 898183/256, Actual: 898183/16"""
