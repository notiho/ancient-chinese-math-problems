"""
今有生鐵六千二百八十一斤欲鍊為黄鐵毎斤耗五兩問為黄鐵幾何
術曰置生鐵數以一十一兩乗以一十六除之即得
答曰黄鐵 a斤
"""

"""
Suppose there are 6281 jin of raw iron. It is desired to refine it into yellow iron, with each jin losing 5 liang.
Question: how much yellow iron is obtained?

The procedure says: Place the number of raw iron. Multiply it by 11 liang (since 1 jin = 16 liang, 16 - 5 = 11). Divide it by 16. This gives the result.

Answer: *a* jin of yellow iron.
"""

# 生鐵六千二百八十一斤
生鐵 = 6281

# 每斤耗五兩，則每斤剩十一兩
每斤剩 = 11

# 一斤等於十六兩
一斤 = 16

# 以一十一兩乘
實 = 生鐵 * 每斤剩

# 以一十六除之，即得
a = Fraction(實, 一斤)
"""
"""
