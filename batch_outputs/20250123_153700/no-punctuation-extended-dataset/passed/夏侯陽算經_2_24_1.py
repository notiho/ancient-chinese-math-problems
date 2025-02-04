"""
今有生鐵六千二百八十一斤欲鍊為黄鐵毎斤耗五兩問為黄鐵幾何
術曰置生鐵數以一十一兩乗以一十六除之即得
答曰黄鐵 a斤
"""

"""
Suppose there are 6281 jin of raw iron. It is desired to refine it into yellow iron, where each jin loses 5 liang.
Question: how much yellow iron is obtained?

The procedure says: Place the number of raw iron. Multiply it by 11 liang (1 jin = 16 liang, so 1 jin - 5 liang = 11 liang). Divide it by 16, and the result is obtained.

Answer: it makes *a* jin of yellow iron.
"""

# 生鐵六千二百八十一斤
生鐵 = 6281

# 每斤耗五兩，剩餘一斤為十一兩
每斤黃鐵 = 11  # liang

# 一斤等於十六兩
一斤 = 16  # liang

# 置生鐵數，以一十一兩乘
實 = 生鐵 * 每斤黃鐵

# 以一十六除之，即得
a = Fraction(實, 一斤)
"""
"""
