"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet. The exchange rate is 8 dou of millet for 5 dou of wheat.
Question: how much wheat is obtained?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560

# 1 斛 = 10 斗, so convert millet to dou
粟_in_斗 = 粟 * 10

# Exchange rate: 8 斗 of millet = 5 斗 of wheat
# Wheat obtained = (millet in dou) * (5 / 8)
麥_in_斗 = 粟_in_斗 * Fraction(5, 8)

# Convert wheat from dou to hu (1 hu = 10 dou)
a = 麥_in_斗 / 10

# Result
a#----- content ends here -----

"""
"""
