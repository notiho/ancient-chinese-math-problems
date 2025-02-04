"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is 1 mu of field, which yields 6 sheng and a little more than half a sheng of millet.
Now there is a field of 1 qing, 26 mu, and 159 bu.
Question: how much millet is harvested?

The procedure says: Take 240 bu per mu as the divisor.
Multiply 6 sheng and a little more than half a sheng by the total area of the field in bu, obtaining the dividend.
Divide the dividend by the divisor, obtaining the amount of millet.

Answer: *a* hu.
"""

from fractions import Fraction

# 1畝收粟6升、太半升
粟每畝 = 6 + Fraction(3, 5)  # 太半升 is interpreted as "a little more than half," often taken as 3/5

# 田一頃二十六畝一百五十九步
畝法 = 240  # 1畝 = 240步
田積步 = (1 * 100 + 26) * 畝法 + 159  # 1頃 = 100畝, convert to total steps

# 以六升、太半升乘今有田積步為實
實 = 粟每畝 * 田積步

# 實如法得粟數
粟數 = Fraction(實, 畝法)

# Convert to 斛 (1斛 = 10升)
a = 粟數 / 10  # Convert sheng to hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 334389/4000"""
