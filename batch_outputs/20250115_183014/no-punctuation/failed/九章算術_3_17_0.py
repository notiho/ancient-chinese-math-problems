"""
今有田一畝收粟六升太半升今有田一頃二十六畝一百五十九步問收粟幾何
術曰以畝二百四十步為法以六升太半升乘今有田積步為實實如法得粟數
荅曰 a斛 
"""

"""
Suppose there is 1 mu of land that yields 6 sheng and a little more than half a sheng of millet.
Now, there is a field of 1 qing, 26 mu, and 159 bu.
Question: how much millet is harvested?

The procedure says: Take 240 bu per mu as the divisor.
Take 6 sheng and a little more than half a sheng, and multiply it by the total number of bu in the field as the dividend.
Divide the dividend by the divisor to obtain the amount of millet.

The answer says: *a* hu.
"""

# 1畝收粟6升太半升
粟每畝 = 6 + Fraction(1, 2)  # 6升太半升 = 6 + 1/2升

# 田一頃二十六畝一百五十九步
畝法 = 240  # 每畝240步
田積步 = 1 * 100 * 畝法 + 26 * 畝法 + 159  # 1頃 = 100畝, 每畝240步

# 以6升太半升乘今有田積步為實
實 = 粟每畝 * 田積步

# 實如法得粟數
粟數 = Fraction(實, 畝法)

# 1斛 = 10升
a = Fraction(粟數, 10)  # 粟數轉換為斛
"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
