"""
今有生鐵六千二百八十一斤欲鍊為黄鐵毎斤耗五兩問為黄鐵幾何
術曰置生鐵數以一十一兩乗以一十六除之即得
答曰黄鐵 a斤
"""

#----- content starts here -----
"""
Suppose there are 6281 jin of raw iron. It is desired to refine it into yellow iron, where each jin loses 5 liang.
Question: how much yellow iron is obtained?

The procedure says: Place the number of raw iron. Multiply it by 11 liang (as 1 jin = 16 liang, and 16 - 5 = 11 liang). Divide it by 16 to convert back to jin. This gives the result.

Answer: *a* jin of yellow iron.
"""

# 生鐵數
生鐵 = 6281

# 每斤耗五兩，剩餘為十一兩
每斤黃鐵 = 11  # liang

# 一斤為十六兩
一斤 = 16  # liang

# 置生鐵數，以一十一兩乘
黃鐵總量 = 生鐵 * 每斤黃鐵

# 以一十六除之，即得
a = Fraction(黃鐵總量, 一斤)#----- content ends here -----

"""
"""
