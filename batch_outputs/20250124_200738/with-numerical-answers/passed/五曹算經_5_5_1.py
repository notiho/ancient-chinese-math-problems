"""
今有生絲一斤為練絲一十二两，有練絲一千五百八十七两。問：生絲㡬何？
術曰：列練絲一千五百八十七两以十六两乘之得二萬五千三百九十二两以十二两除之即得。
答曰： a(=2116)两 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk, which produces 12 liang of refined silk.
Now, there are 1587 liang of refined silk.
Question: how much raw silk is required?

The procedure says: Place 1587 liang of refined silk, multiply it by 16 liang [per jin], obtaining 25392 liang.
Divide it by 12 liang [per jin of raw silk], and the result is obtained.

Answer: *a*(=2116) liang of raw silk.
"""

# 練絲一千五百八十七两
練絲 = 1587

# 一斤等於十六两
一斤 = 16

# 生絲一斤為練絲一十二两
練絲率 = 12

# 以十六两乘之
總生絲量 = 練絲 * 一斤

# 以十二两除之即得
a = Fraction(總生絲量, 練絲率) # 2116
#----- content ends here -----

"""
"""
