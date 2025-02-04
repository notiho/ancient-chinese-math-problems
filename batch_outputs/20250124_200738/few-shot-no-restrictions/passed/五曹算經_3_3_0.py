"""
今有粟三百六十二斛。問：為御米㡬何？
術曰：列粟三百六十二斛，以二十一升乘之得七千六百二斛，以五十除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 362 hu of millet. 
Question: how much polished rice can be obtained?

The procedure says: Place 362 hu of millet, multiply it by 21 sheng, obtaining 7602 hu. 
Divide it by 50 to get the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟三百六十二斛
粟 = 362

# 每斛粟以二十一升乘之
每斛轉化率 = 21

# 乘之得七千六百二斛
總量 = 粟 * 每斛轉化率

# 以五十除之即得
a = Fraction(總量, 50)

# Output the result
a#----- content ends here -----

"""
"""
