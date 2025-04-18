"""
今有生絲一斤為練絲一十二两，有練絲一千五百八十七两。問：生絲㡬何？
術曰：列練絲一千五百八十七两以十六两乘之得二萬五千三百九十二两以十二两除之即得。
答曰： a两 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of raw silk that produces 12 liang of refined silk.
Now, there are 1587 liang of refined silk.
Question: how much raw silk is required?

The procedure says: Place the 1587 liang of refined silk and multiply it by 16 liang [per jin], obtaining 25392 liang.
Divide it by 12 liang, and the result is obtained.

Answer: *a* liang.
"""
#NO_ERR

# 練絲一千五百八十七两
練絲 = 1587

# 以十六两乘之
總量 = 練絲 * 16

# 以十二两除之即得
a = Fraction(總量, 12)#----- content ends here -----

"""
"""
