"""
今有粟二斗一升。問：為粺米幾何？
術曰：置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實；以粟率五十為法，除之不盡，以法而命分。
答曰： a斗 。
"""

"""
Suppose there are 2 dou and 1 sheng of millet. 
Question: how much polished rice does it make?

The procedure says: Place the millet amount, 21 sheng. 
Multiply it by the polished rice rate, 27, obtaining 567 sheng as the dividend. 
Take the millet rate, 50, as the divisor. 
Divide the dividend by the divisor. If there is a remainder, express it as a fraction of the divisor.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟二斗一升
粟 = 2 * 10 + 1  # Convert to sheng (1 dou = 10 sheng)

# 粺米率二十七
粺米率 = 27

# 粟率五十
粟率 = 50

# 以粺米率二十七乘之，得五百六十七升，為實
實 = 粟 * 粺米率

# 以粟率五十為法，除之不盡，以法而命分
a = Fraction(實, 粟率)  # Result in dou (1 dou = 10 sheng)

# Convert to dou
a_dou = a / 10  # Convert sheng to dou if needed
"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 567/50"""
