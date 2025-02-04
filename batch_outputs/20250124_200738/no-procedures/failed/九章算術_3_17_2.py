"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
荅曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 1 mu of land, which yields 6 sheng and 0.5 sheng of millet (6.5 sheng in total).  
Now, there is 1 qing, 26 mu, and 159 bu of land.  
Question: how much millet is harvested?

Answer: it yields *a* hu.
"""

# 1 畝 yields 6.5 升
yield_per_mu = Fraction(13, 2)  # 6.5 sheng

# 1 頃 = 100 畝
qing_to_mu = 100

# 1 畝 = 240 步
mu_to_bu = 240

# Total land in mu
land_in_mu = 1 * qing_to_mu + 26 + Fraction(159, mu_to_bu)

# Total yield in sheng
total_yield_in_sheng = yield_per_mu * land_in_mu

# 1 斛 = 10 升
sheng_to_hu = 10

# Convert total yield to hu
a = total_yield_in_sheng / sheng_to_hu

# Final result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
