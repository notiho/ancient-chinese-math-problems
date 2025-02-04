"""
今有粟二斗一升。問：為粺米幾何？
術曰：置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實；以粟率五十為法，除之不盡，以法而命分。
答曰： a(=567/500)斗 。
"""

"""
Suppose there are 2 dou and 1 sheng of millet. 
Question: how much polished rice does it make?

The procedure says: Place the amount of millet, 21 sheng, and multiply it by the polished rice rate, 27, obtaining 567 sheng as the dividend.
Take the millet rate, 50, as the divisor.
Divide the dividend by the divisor. If there is a remainder, express it as a fraction of the divisor.

Answer: *a*(=567/500) dou.
"""

from fractions import Fraction

# 粟二斗一升
粟斗 = 2
粟升 = 1

# Convert to 升 (1 斗 = 10 升)
粟數 = (粟斗 * 10) + 粟升

# 粺米率二十七
粺米率 = 27

# 置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實
實 = 粟數 * 粺米率

# 粟率五十為法
法 = 50

# 除之不盡，以法而命分
a = Fraction(實, 法) # 567/500
"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 567/50"""
