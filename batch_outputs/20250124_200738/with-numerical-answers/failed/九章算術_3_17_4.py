"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a(=10133/1200)斛 。
"""

#----- content starts here -----
"""
Suppose there is a field of 1 mu, yielding 6 sheng and a half sheng of millet.
Now, there is a field of 1 qing, 26 mu, and 159 bu.
Question: how much millet is harvested?

The procedure says: Take 240 bu per mu as the divisor.
Multiply 6 sheng and a half sheng by the total area of the field in bu to get the dividend.
Divide the dividend by the divisor to obtain the amount of millet.

Answer: *a*(=10133/1200) hu.
"""

from fractions import Fraction

# 田一畝，收粟六升、太半升
畝收粟 = 6 + Fraction(1, 2)  # 6.5 升

# 畝二百四十步為法
畝步數 = 240  # 每畝 240 步

# 今有田一頃二十六畝一百五十九步
頃 = 100  # 1 頃 = 100 畝
田積步 = (1 * 頃 + 26) * 畝步數 + 159  # 將田積轉換為步數

# 以六升、太半升乘今有田積步為實
實 = 畝收粟 * 田積步

# 實如法得粟數
粟數 = Fraction(實, 畝步數)

# 1 斛 = 10 升
a = 粟數 / 10  # 將粟數轉換為斛 (10133/1200 斛)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
