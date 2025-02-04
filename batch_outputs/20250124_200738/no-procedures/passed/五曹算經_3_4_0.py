"""
今有粟五百六十斛，凡粟八斗易麥五斗。問：得麥㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet, and for every 8 dou of millet, 5 dou of wheat can be exchanged.
Question: how much wheat can be obtained?

Answer: *a* hu.
"""

from fractions import Fraction

# 粟五百六十斛
粟 = 560

# 1 hu = 10 dou, so convert millet into dou
粟_in_dou = 粟 * 10

# For every 8 dou of millet, 5 dou of wheat is obtained
exchange_rate = Fraction(5, 8)

# Calculate the amount of wheat in dou
wheat_in_dou = 粟_in_dou * exchange_rate

# Convert wheat back into hu (1 hu = 10 dou)
a = Fraction(wheat_in_dou, 10)

# Result
a#----- content ends here -----

"""
"""
