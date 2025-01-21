"""
今有黄鐵三千七十六斤一十四兩一十三分兩之一十卻求鋼鐵問得幾何
術曰置黄鐵數一十三乗之一十六除之即得
答曰 a斤
"""

"""
Suppose there is 3076 jin, 14 liang, and 13/10 of a liang of yellow iron.
Question: how much steel does it yield?

The procedure says: Place the amount of yellow iron. Multiply it by 13 and divide by 16 to obtain the result.

Answer: *a* jin.
"""

from fractions import Fraction

# 黄鐵三千七十六斤一十四兩一十三分兩之一十
黃鐵 = 3076  # 斤
黃鐵 += Fraction(14, 16)  # 14兩 converted to 斤 (16兩 = 1斤)
黃鐵 += Fraction(13, 10 * 16)  # 13/10兩 converted to 斤

# 一十三乗之一十六
鋼鐵 = 黃鐵 * Fraction(13, 16)

# 答曰 a斤
a = 鋼鐵
"""
Variable 'a' has wrong value. Expected: 2500, Actual: 6400069/2560"""
