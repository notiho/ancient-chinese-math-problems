"""
今有粟三百六十二斛。問：為御米㡬何？
術曰：列粟三百六十二斛，以二十一升乘之得七千六百二斛，以五十除之即得。
答曰： a斛 。
"""

"""
Suppose there are 362 hu of millet. 
Question: how much polished rice does it make?

The procedure says: Place the 362 hu of millet. Multiply it by 21 sheng, obtaining 7602 hu. 
Divide it by 50, and the result is obtained.

Answer: *a* hu.
"""

# 粟三百六十二斛
粟 = 362

# 以二十一升乘之
實 = 21 * 粟

# 以五十除之即得
a = Fraction(實, 50)
"""
"""
