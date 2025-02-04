"""
今有田一畝收粟六升太半升今有田一頃二十六畝一百五十九步問收粟幾何
術曰以畝二百四十步為法以六升太半升乘今有田積步為實實如法得粟數
荅曰 a斛 
"""

#----- content starts here -----
"""
Suppose there is 1 mu of field that yields 6 sheng and a little more than half a sheng of millet.
Now there is a field of 1 qing, 26 mu, and 159 bu.
Question: how much millet is harvested?

The procedure says: Take 240 bu per mu as the divisor.
Multiply 6 sheng and a little more than half a sheng by the total number of bu in the field, obtaining the dividend.
Divide the dividend by the divisor, obtaining the amount of millet.

The answer says: *a* hu.
"""

from fractions import Fraction

# 每畝收粟六升太半升
每畝收粟 = 6 + Fraction(1, 2)

# 田一頃二十六畝一百五十九步
田積步 = (1 * 100 * 240) + (26 * 240) + 159  # 1 qing = 100 mu, 1 mu = 240 bu

# 畝二百四十步為法
畝法 = 240

# 以六升太半升乘今有田積步為實
實 = 每畝收粟 * 田積步

# 實如法得粟數
粟數 = Fraction(實, 畝法)

# 1 斛 = 10 升
a = 粟數 / 10  # Convert sheng to hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
