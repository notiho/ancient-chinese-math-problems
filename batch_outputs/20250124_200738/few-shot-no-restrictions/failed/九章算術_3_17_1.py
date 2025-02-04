"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 1 mu of land, which yields 6 sheng and 1/2 sheng of millet.
Now, there is 1 qing, 26 mu, and 159 bu of land.
Question: how much millet is harvested?

The procedure says: Take 240 bu per mu as the divisor.
Multiply 6 sheng and 1/2 sheng by the total area of the land in bu, obtaining the dividend.
Divide the dividend by the divisor to get the total millet yield.

Answer: *a* hu.
"""

from fractions import Fraction

# 1 畝 yields 6 升 and 太半升 (1/2 升)
yield_per_mu = 6 + Fraction(1, 2)  # 6.5 升 per 畝

# 田積: 1 頃, 26 畝, 159 步
qing_to_mu = 100  # 1 頃 = 100 畝
mu_to_bu = 240    # 1 畝 = 240 步

田積步 = (1 * qing_to_mu + 26) * mu_to_bu + 159  # Total area in 步

# 畝法: 240 步 per 畝
畝法 = 240

# Multiply yield per 畝 by total area in 步
實 = yield_per_mu * 田積步

# Divide by 畝法 to get total millet yield in 升
total_millet_sheng = Fraction(實, 畝法)

# Convert 升 to 斛 (1 斛 = 10 升)
a = total_millet_sheng / 10  # Total yield in 斛

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
