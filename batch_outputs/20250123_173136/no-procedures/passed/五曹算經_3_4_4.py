"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
答曰： a斛 。
"""

"""
Suppose there are 560 hu of millet. For every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat can be obtained?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560

# 1 hu = 10 dou, so convert millet to dou
粟_in_dou = 粟 * 10

# Exchange rate: 8 dou of millet = 5 dou of wheat
# Wheat obtained in dou
wheat_in_dou = Fraction(5, 8) * 粟_in_dou

# Convert wheat back to hu
a = wheat_in_dou / 10

# Result
a
"""
"""
