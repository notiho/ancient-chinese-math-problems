"""
今有粟二百九十斛。問：為粺米㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 290 hu of unhusked millet. It is desired to turn it into polished rice.
Question: how much polished rice does it make?

Answer: it makes *a* hu.
"""

from fractions import Fraction

# 粟二百九十斛
粟 = 290

# To convert unhusked millet to polished rice, multiply by 2/3
a = Fraction(2, 3) * 粟

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 783/5, Actual: 580/3"""
