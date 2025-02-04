"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 1 mu of land, which yields 6 sheng and a little more than half a sheng of millet.
Now, there is a field of 1 qing, 26 mu, and 159 bu. 
Question: how much millet will it yield?

The procedure says: Take 240 bu per mu as the divisor.
Multiply 6 sheng and a little more than half a sheng by the total area of the field in bu to get the dividend.
Divide the dividend by the divisor to obtain the total millet yield.

Answer: *a* hu.
"""

from fractions import Fraction

# 1 畝 yields 6 升 and 太半升 (太半升 = 1/2 升 + 1/10 升)
yield_per_mu = 6 + Fraction(1, 2) + Fraction(1, 10)

# 田一頃二十六畝一百五十九步
# 1 頃 = 100 畝
qing = 1
mu = 26
bu = 159

# Convert the total area to 步
total_area_in_bu = (qing * 100 + mu) * 240 + bu

# 畝法二百四十步
mu_in_bu = 240

# Multiply yield per 畝 by total area in 步 to get the total yield in 升
total_yield_in_sheng = yield_per_mu * total_area_in_bu

# Convert 升 to 斛 (1 斛 = 10 升)
total_yield_in_hu = total_yield_in_sheng / 10

# Answer
a = total_yield_in_hu
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 1003167/50"""
