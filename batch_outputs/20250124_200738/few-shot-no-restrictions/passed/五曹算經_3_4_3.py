"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
術曰：列粟五百六十斛，以五十乘之得二萬八千斛，以八千除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet. For every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat is obtained?

The procedure says: Place the 560 hu of millet. Multiply it by 50, obtaining 28000 dou. Divide it by 8000, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560  # in hu

# 1 hu = 10 dou, so convert 粟 to dou
粟_dou = 10 * 粟

# 每八斗粟易五斗麥
粟_to_麥_ratio = Fraction(5, 8)

# 計算麥的數量
麥_dou = 粟_dou * 粟_to_麥_ratio

# 將麥的數量從斗轉換為斛 (1 hu = 10 dou)
a = 麥_dou / 10  # in hu

a#----- content ends here -----

"""
"""
