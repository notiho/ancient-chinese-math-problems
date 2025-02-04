"""
今有粟三百六十二斛問為御米㡬何
術曰列粟三百六十二斛以二十一升乘之得七千六百二斛以五十除之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there are 362 hu of millet.
Question: how much polished rice does it make?

The procedure says: Place the 362 hu of millet.
Multiply it by 21 sheng, obtaining 7602 hu.
Divide it by 50, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟三百六十二斛
粟 = 362

# 以二十一升乘之
實 = 21 * 粟

# 以五十除之
a = Fraction(實, 50)#----- content ends here -----

"""
"""
