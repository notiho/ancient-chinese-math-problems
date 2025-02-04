"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
荅曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 1 mu of field that yields 6 sheng and 0.5 sheng of millet.  
Now, there is a field of 1 qing, 26 mu, and 159 bu.  
Question: how much millet is harvested?

Answer: it yields *a* hu of millet.
"""

from fractions import Fraction

# Yield per mu
yield_per_mu = 6 + Fraction(1, 2)  # 6.5 sheng per mu

# Field size in mu
# 1 qing = 100 mu, so 1 qing + 26 mu + 159 bu
# 1 mu = 240 bu, so 159 bu = 159 / 240 mu
field_size_mu = 100 + 26 + Fraction(159, 240)

# Total yield in sheng
total_yield_sheng = yield_per_mu * field_size_mu

# Convert sheng to hu
# 1 hu = 10 dou, 1 dou = 10 sheng, so 1 hu = 100 sheng
a = Fraction(total_yield_sheng, 100)  # Convert sheng to hu

a  # Output the total yield in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/16000"""
