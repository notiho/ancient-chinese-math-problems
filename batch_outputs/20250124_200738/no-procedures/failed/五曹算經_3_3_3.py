"""
今有粟三百六十二斛。問：為御米㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 362 hu of unhusked millet. It is desired to turn it into polished rice.
Question: how much polished rice does it make?

Answer: it makes *a* hu of polished rice.
"""

# 粟三百六十二斛
粟 = 362

# To convert unhusked millet to polished rice, multiply by 2/3
a = Fraction(2 * 粟, 3)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3801/25, Actual: 724/3"""
