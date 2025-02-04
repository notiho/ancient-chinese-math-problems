"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a(=10133/1200)斛 。
"""

"""
Suppose there is a field of 1 mu, which yields 6 sheng and a little more than half a sheng of millet.
Now, suppose there is a field of 1 qing, 26 mu, and 159 bu. 
Question: how much millet does it yield?

The procedure says: Take 240 bu per mu as the divisor. 
Multiply 6 sheng and a little more than half a sheng by the total field area in bu to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of millet.

Answer: *a*(=10133/1200) hu.
"""

from fractions import Fraction

# 每畝收粟六升、太半升
每畝收粟 = 6 + Fraction(3, 5)  # 太半升 = 3/5 升

# 田一頃二十六畝一百五十九步
一頃 = 100  # 1 頃 = 100 畝
畝步數 = 240  # 每畝 240 步
田積步 = (1 * 一頃 + 26) * 畝步數 + 159  # 田積步 = 總步數

# 以畝二百四十步為法
法 = 畝步數

# 以六升、太半升乘今有田積步為實
實 = 每畝收粟 * 田積步

# 實如法得粟數
a = Fraction(實, 法) / 10  # 1 斛 = 10 升

a  # 10133/1200 hu
"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 334389/4000"""
