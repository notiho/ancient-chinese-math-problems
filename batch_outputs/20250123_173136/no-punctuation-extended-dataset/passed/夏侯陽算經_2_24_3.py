"""
今有生鐵六千二百八十一斤欲鍊為黄鐵毎斤耗五兩問為黄鐵幾何
術曰置生鐵數以一十一兩乗以一十六除之即得
答曰黄鐵 a斤
"""

"""
Suppose there are 6281 jin of raw iron. It is desired to refine it into yellow iron, where each jin loses 5 liang.
Question: how many jin of yellow iron does it make?

The procedure says: Place the number of raw iron. Multiply it by 11 liang (1 jin = 16 liang, so 11 liang = 11/16 jin). Divide it by 16 to obtain the result.

Answer: it makes *a* jin of yellow iron.
"""

from fractions import Fraction

# 生鐵六千二百八十一斤
生鐵 = 6281

# 每斤耗五兩 (1 斤 = 16 兩, 所以每斤剩餘 11 兩)
耗率 = Fraction(11, 16)

# 置生鐵數，以一十一兩乘
實 = 生鐵 * 耗率

# 以一十六除之，即得
a = 實

# Output the result
a
"""
"""
