"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
荅曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 1 mu of land that yields 6 sheng and 0.5 sheng of millet (6.5 sheng in total).
Now, there is 1 qing, 26 mu, and 159 bu of land. 
Question: how much millet is harvested?

Answer: it yields *a* hu.
"""

from fractions import Fraction

# Yield per mu
yield_per_mu = Fraction(6) + Fraction(1, 2)  # 6.5 sheng

# Convert land area into mu
# 1 qing = 100 mu, and 240 bu = 1 mu
land_in_mu = 1 * 100 + 26 + Fraction(159, 240)

# Total yield in sheng
total_yield_in_sheng = yield_per_mu * land_in_mu

# Convert sheng to hu (1 hu = 10 sheng)
a = total_yield_in_sheng / 10  # Result in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
