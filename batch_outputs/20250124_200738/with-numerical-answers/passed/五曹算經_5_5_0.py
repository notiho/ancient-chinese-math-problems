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

The procedure says: Place 1587 liang of refined silk, multiply it by 16 liang (since 1 jin = 16 liang), obtaining 25392 liang.
Divide this by 12 liang, and the result is the amount of raw silk.

Answer: *a*(=2116) liang.
"""

# 練絲一千五百八十七两
練絲 = 1587

# 以十六两乘之
實 = 16 * 練絲

# 以十二两除之即得
a = Fraction(實, 12) # 2116 (两 of 生絲)#----- content ends here -----

"""
"""
