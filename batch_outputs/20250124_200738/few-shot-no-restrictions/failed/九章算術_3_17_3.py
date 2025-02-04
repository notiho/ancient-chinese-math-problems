"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 1 mu of land that yields 6 sheng and 1/2 sheng of millet. 
Now, there is a field of 1 qing, 26 mu, and 159 bu. 
Question: how much millet is harvested?

The procedure says: Take 240 bu per mu as the divisor. 
Multiply 6 sheng and 1/2 sheng by the total area of the field in bu to obtain the dividend. 
Divide the dividend by the divisor to get the total amount of millet.

Answer: *a* hu.
"""

from fractions import Fraction

# 1 畝 yields 6 sheng and 1/2 sheng
yield_per_mu = 6 + Fraction(1, 2)  # 6.5 sheng

# 1 畝 = 240 步
步_per_mu = 240

# Total field area: 1 頃, 26 畝, 159 步
# 1 頃 = 100 畝
total_mu = 1 * 100 + 26  # 126 畝
total_bu = total_mu * 步_per_mu + 159  # Convert to total 步

# Multiply yield per 畝 by total field area in 步
實 = yield_per_mu * total_bu

# Divide by 步_per_mu to get total yield in sheng
total_sheng = Fraction(實, 步_per_mu)

# Convert sheng to hu (1 hu = 10 sheng)
a = Fraction(total_sheng, 10)  # Convert to hu

a  # Total yield in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
