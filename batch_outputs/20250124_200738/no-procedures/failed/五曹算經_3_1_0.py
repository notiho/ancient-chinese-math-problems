"""
今有粟二百九十斛。問：為粺米㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 290 hu of unhusked millet. It is desired to turn it into polished millet.
Question: how much polished millet does it make?

Answer: it makes *a* hu.
"""

from fractions import Fraction

# 粟二百九十斛
粟 = 290

# Polished millet is obtained by multiplying the unhusked millet by 7/10
a = Fraction(7 * 粟, 10)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 783/5, Actual: 203"""
