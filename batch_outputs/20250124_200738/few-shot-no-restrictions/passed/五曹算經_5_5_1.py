"""
今有生絲一斤為練絲一十二两，有練絲一千五百八十七两。問：生絲㡬何？
術曰：列練絲一千五百八十七两以十六两乘之得二萬五千三百九十二两以十二两除之即得。
答曰： a两 。
"""

#----- content starts here -----
"""
Suppose there is raw silk, 1 jin of which produces 12 liang of refined silk.
Now, there are 1587 liang of refined silk.
Question: how much raw silk is required?

The procedure says: Place the 1587 liang of refined silk, multiply it by 16 liang (since 1 jin = 16 liang), obtaining 25392 liang.
Then divide it by 12 liang, obtaining the result.

Answer: *a* liang of raw silk.
"""

from fractions import Fraction

# 練絲一千五百八十七两
練絲 = 1587

# 1斤 = 16两
一斤 = 16

# 生絲1斤為練絲12两
練絲率 = 12

# 以十六两乘之
總生絲量 = 練絲 * 一斤

# 以十二两除之
a = Fraction(總生絲量, 練絲率)

# Output the result
a#----- content ends here -----

"""
"""
