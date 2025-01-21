"""
今有生絲一斤為練絲一十二两有練絲一千五百八十七两問生絲㡬何
術曰列練絲一千五百八十七两以十六两乘之得二萬五千三百九十二两以十二两除之即得
答曰 a 两
"""

"""
Suppose there is 1 jin of raw silk, which produces 12 liang of refined silk.
Now, there are 1587 liang of refined silk.
Question: how much raw silk is required?

The procedure says: Place the 1587 liang of refined silk.
Multiply it by 16 liang (to convert jin to liang), obtaining 25392 liang.
Divide it by 12 liang, and the result is obtained.

Answer: *a* liang of raw silk.
"""

# 練絲一千五百八十七两
練絲 = 1587

# 以十六两乘之
總量 = 16 * 練絲

# 以十二两除之
a = Fraction(總量, 12)
"""
"""
