"""
今有粟三百六十二斛。問：為御米㡬何？
術曰：列粟三百六十二斛，以二十一升乘之得七千六百二斛，以五十除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 362 hu of millet. 
Question: how much polished rice can be obtained?

The procedure says: Take the 362 hu of millet, multiply it by 21 sheng, obtaining 7602 sheng. 
Divide it by 50, and the result is the amount of polished rice.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟三百六十二斛
粟 = 362

# 每斛 21 升
升每斛 = 21

# 以二十一升乘之得七千六百二斛
總升 = 粟 * 升每斛

# 每 50 升為 1 斛
升每斛標準 = 50

# 以五十除之即得
a = Fraction(總升, 升每斛標準)

# 答案
a#----- content ends here -----

"""
"""
