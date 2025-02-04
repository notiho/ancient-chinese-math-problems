"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
答曰： a斛 。
"""

"""
Suppose there are 560 hu of millet. The exchange rate is 8 dou of millet for 5 dou of wheat.
Question: how much wheat can be obtained?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560

# 1 hu = 10 dou, so convert millet to dou
粟斗 = 粟 * 10

# Exchange rate: 8 dou of millet = 5 dou of wheat
# Wheat obtained = (粟斗 * 5) / 8
麥斗 = Fraction(粟斗 * 5, 8)

# Convert wheat from dou to hu (1 hu = 10 dou)
a = 麥斗 / 10

# Result
a
"""
"""
