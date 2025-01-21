"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a(=10133/1200)斛 。
"""

"""
Suppose there is a field of 1 mu, which yields 6 sheng and a little more than half a sheng of millet.
Now suppose there is a field of 1 qing, 26 mu, and 159 bu.
Question: how much millet does it yield?

The procedure says: Take 240 bu per mu as the divisor.
Multiply 6 sheng and a little more than half a sheng by the total area of the field in bu, obtaining the dividend.
Divide the dividend by the divisor to obtain the total millet yield.

Answer: *a*(=10133/1200) hu.
"""

from fractions import Fraction

# 每畝收粟六升、太半升
每畝收粟 = 6 + Fraction(3, 5)  # 太半升 = 3/5升

# 每畝為二百四十步
畝法 = 240

# 今有田一頃二十六畝一百五十九步
田積步 = (1 * 100 + 26) * 畝法 + 159  # 1頃 = 100畝

# 以六升、太半升乘今有田積步為實
實 = 每畝收粟 * 田積步

# 實如法得粟數
a = Fraction(實, 畝法)  # 10133/1200 hu
"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 334389/400"""
