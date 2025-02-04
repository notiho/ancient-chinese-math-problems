"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
荅曰： a斛 。
"""

"""
Suppose there is 1 mu of land that yields 6 sheng and half a sheng of millet.
Now, there is a field of 1 qing, 26 mu, and 159 bu. 
Question: how much millet does it yield?

Answer: it yields *a* hu.
"""

from fractions import Fraction

# Yield per mu
yield_per_mu = 6 + Fraction(1, 2)  # 6 sheng and half a sheng

# Convert the field size into mu
# 1 qing = 100 mu, 1 mu = 240 bu
field_in_mu = 1 * 100 + 26 + Fraction(159, 240)

# Total yield in sheng
total_yield_in_sheng = yield_per_mu * field_in_mu

# Convert sheng to hu (1 hu = 10 sheng)
a = Fraction(total_yield_in_sheng, 10)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
