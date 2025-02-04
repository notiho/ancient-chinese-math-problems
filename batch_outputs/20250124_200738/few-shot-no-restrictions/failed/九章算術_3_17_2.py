"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 1 mu of land, which yields 6 sheng and a little more than half a sheng of millet.
Now, there is a field of 1 qing, 26 mu, and 159 bu. 
Question: how much millet does it yield?

The procedure says: Take 240 bu per mu as the divisor. 
Multiply the yield of 6 sheng and a little more than half a sheng by the total area of the field in bu to get the dividend.
Divide the dividend by the divisor to get the total millet yield.

Answer: *a* hu.
"""

from fractions import Fraction

# 每畝收粟 6 升、太半升
粟每畝 = 6 + Fraction(3, 5)  # 太半升 is interpreted as "a little more than half," often taken as 3/5.

# 田一頃二十六畝一百五十九步
畝法 = 240  # 每畝 240 步
田積步 = (1 * 100 + 26) * 畝法 + 159  # 1 頃 = 100 畝, 1 畝 = 240 步

# 以 6 升、太半升乘今有田積步為實
實 = 粟每畝 * 田積步

# 實如法得粟數
粟數 = Fraction(實, 畝法)

# 1 斛 = 10 升
a = Fraction(粟數, 10)  # 轉換為斛

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 334389/4000"""
