"""
今有粟二百九十斛。問：為粺米㡬何？
術曰：列粟二百九十斛，以二十七乘之得七千八百三十斛，以五十除之即得。
答曰： a斛 。
"""

"""
Suppose there are 290 hu of unhusked millet.
Question: how much polished millet does it make?

The procedure says: Place the 290 hu of unhusked millet.
Multiply it by 27, obtaining 7830 hu.
Divide it by 50, and the result is obtained.

Answer: *a* hu.
"""

# 粟二百九十斛
粟 = 290

# 以二十七乘之
積 = 27 * 粟

# 以五十除之即得
a = Fraction(積, 50)
"""
"""
