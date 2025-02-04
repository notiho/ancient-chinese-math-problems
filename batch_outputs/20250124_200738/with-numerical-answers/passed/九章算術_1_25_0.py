"""
又有圭田廣五步、二分步之一，從八步、三分步之二。問：為田幾何？
術曰：半廣以乘正從。
荅曰： a(=143/6)步 。
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a width of 5 bu and 1/2 bu, and a length of 8 bu and 2/3 bu.
Question: how large is the field?

The procedure says: Take half the width and multiply it by the full length.

Answer: *a*(=143/6) bu.
"""

from fractions import Fraction

# 廣五步、二分步之一
廣 = 5 + Fraction(1, 2)

# 從八步、三分步之二
從 = 8 + Fraction(2, 3)

# 半廣以乘正從
半廣 = 廣 / 2
a = 半廣 * 從 # 143/6#----- content ends here -----

"""
"""
