"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a field of 1 mu, which yields 6 sheng and 1/2 sheng of millet.
Now, there is a field of 1 qing, 26 mu, and 159 bu.
Question: how much millet does it yield?

The procedure says: Take 240 bu per mu as the divisor.
Multiply 6 sheng and 1/2 sheng by the total area of the field in bu to obtain the dividend.
Divide the dividend by the divisor to obtain the total millet yield.

Answer: *a* hu.
"""

from fractions import Fraction

# 1 畝 yields 6 升 and 太半升 (1/2 升)
yield_per_mu = 6 + Fraction(1, 2)  # in 升

# 1 畝 = 240 步
步_per_mu = 240

# Total field area: 1 頃, 26 畝, 159 步
# 1 頃 = 100 畝
total_field_in_mu = 1 * 100 + 26 + Fraction(159, 步_per_mu)  # Convert 步 to 畝

# Convert total field area to 步
total_field_in_bu = total_field_in_mu * 步_per_mu

# Multiply yield per 畝 by total field area in 步
total_yield_in_sheng = yield_per_mu * total_field_in_bu

# Divide by 步_per_mu to get the total yield in 升
total_yield_in_sheng = total_yield_in_sheng / 步_per_mu

# Convert 升 to 斛 (1 斛 = 10 升)
a = total_yield_in_sheng / 10  # in 斛

a  # Total yield in 斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
