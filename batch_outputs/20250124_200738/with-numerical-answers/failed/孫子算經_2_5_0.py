"""
今有粟二斗一升。問：為粺米幾何？
術曰：置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實；以粟率五十為法，除之不盡，以法而命分。
答曰： a(=567/500)斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 1 sheng of millet. 
Question: how much polished rice does it make?

The procedure says: Place the millet amount as 21 sheng. Multiply it by the polished rice rate, 27, obtaining 567 sheng as the dividend. 
Take the millet rate, 50, as the divisor. Divide it, and if there is a remainder, use the divisor to assign the fraction.

Answer: *a*(=567/500) dou.
"""

from fractions import Fraction

# 粟二斗一升
粟斗 = 2
粟升 = 1
粟數 = 10 * 粟斗 + 粟升  # Convert to sheng (1 dou = 10 sheng)

# 粺米率二十七
粺米率 = 27

# 置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實
實 = 粟數 * 粺米率

# 粟率五十為法
粟率 = 50

# 除之不盡，以法而命分
a = Fraction(實, 粟率)  # 567/500 dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 567/50"""
