"""
今有黄鐵三千七十六斤一十四兩一十三分兩之一十卻求鋼鐵問得幾何
術曰置黄鐵數一十三乗之一十六除之即得
答曰 a斤
"""

#----- content starts here -----
"""
Suppose there are 3076 jin, 14 liang, and 13/10 of a liang of yellow iron.
Question: how much steel does it yield?

The procedure says: Place the amount of yellow iron. Multiply it by 13 and divide it by 16. This gives the result.

Answer: *a* jin.
"""

from fractions import Fraction

# 黄鐵三千七十六斤一十四兩一十三分兩之一十
黃鐵_斤 = 3076
黃鐵_兩 = 14
黃鐵_分 = Fraction(13, 10)

# Convert everything to jin (16 liang = 1 jin)
黃鐵 = 黃鐵_斤 + Fraction(黃鐵_兩, 16) + Fraction(黃鐵_分, 16)

# 一十三乗之一十六除之
鋼鐵 = 黃鐵 * Fraction(13, 16)

# Result
a = 鋼鐵#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2500, Actual: 6400069/2560"""
