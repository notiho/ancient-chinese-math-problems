"""
今有粟二百九十斛。問：為粺米㡬何？
術曰：列粟二百九十斛，以二十七乘之得七千八百三十斛，以五十除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 290 hu of unhusked millet. 
Question: how much polished rice does it make?

The procedure says: Take the 290 hu of millet and multiply it by 27, obtaining 7830 hu.
Divide it by 50 to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟二百九十斛
粟 = 290

# 以二十七乘之
積 = 27 * 粟

# 以五十除之即得
a = Fraction(積, 50)

# Output the result
a#----- content ends here -----

"""
"""
