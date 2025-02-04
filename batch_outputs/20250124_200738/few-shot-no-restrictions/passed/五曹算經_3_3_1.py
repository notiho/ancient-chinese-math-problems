"""
今有粟三百六十二斛。問：為御米㡬何？
術曰：列粟三百六十二斛，以二十一升乘之得七千六百二斛，以五十除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 362 hu of millet. 
Question: how much polished rice does it make?

The procedure says: Place the 362 hu of millet. Multiply it by 21 sheng, obtaining 7602 hu. 
Divide it by 50, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟三百六十二斛
粟 = 362

# 每斛粟轉化為御米的比例：以二十一升乘之
轉化比例 = 21

# 以五十除之
除數 = 50

# 計算御米
御米 = Fraction(粟 * 轉化比例, 除數)

a = 御米
print(f"御米: {a} 斛")#----- content ends here -----

"""
"""
