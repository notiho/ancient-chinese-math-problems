"""
今有粟二百九十斛。問：為粺米㡬何？
術曰：列粟二百九十斛，以二十七乘之得七千八百三十斛，以五十除之即得。
答曰： a(=783/5)斛 。
"""

"""
Suppose there are 290 hu of unhusked millet.
Question: how much polished rice does it make?

The procedure says: Place the 290 hu of millet.
Multiply it by 27, obtaining 7830 hu.
Divide it by 50, and the result is obtained.

Answer: *a*(=783/5) hu.
"""

# 粟二百九十斛
粟 = 290

# 以二十七乘之得七千八百三十斛
實 = 27 * 粟

# 以五十除之即得
a = Fraction(實, 50) # 783/5
"""
"""
