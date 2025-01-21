"""
今有黄鐵四千三百一十八斤三兩欲鍊為鋼鐵毎斤耗三兩問鋼鐵幾何
術曰置黄鐵數以一十三兩乗之一十六兩除之即得
答曰鋼鐵 a斤 b 絫
"""

"""
Suppose there are 4318 jin and 3 liang of yellow iron. It is desired to refine it into steel. 
For every jin, 3 liang are consumed.
Question: how much steel is obtained?

The procedure says: Place the amount of yellow iron. 
Multiply it by 13 liang (16 liang per jin minus 3 liang consumed). 
Divide it by 16 liang per jin to obtain the result.

Answer: *a* jin and *b* liang of steel.
"""

from fractions import Fraction

# 黄鐵四千三百一十八斤三兩
黃鐵_斤 = 4318
黃鐵_兩 = 3

# Convert 黃鐵 to total liang (1 斤 = 16 兩)
黃鐵_總兩 = 黃鐵_斤 * 16 + 黃鐵_兩

# 每斤耗三兩, so remaining steel per jin is 16 - 3 = 13 liang
鋼鐵_每斤_兩 = 13

# Multiply 黃鐵_總兩 by 13 (remaining steel per jin)
鋼鐵_總兩 = 黃鐵_總兩 * 鋼鐵_每斤_兩

# Divide by 16 (to convert back to jin and liang)
鋼鐵_總斤 = Fraction(鋼鐵_總兩, 16)

# Extract the integer part (jin) and the remainder (liang)
a = 鋼鐵_總斤.numerator // 鋼鐵_總斤.denominator  # Integer part (jin)
b = 鋼鐵_總斤.numerator % 鋼鐵_總斤.denominator  # Remainder (liang)
"""
Variable 'a' has wrong value. Expected: 673637/192, Actual: 56136
Variable 'b' has wrong value. Expected: 5, Actual: 7"""
