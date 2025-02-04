"""
今有粟二斗一升問為粺米幾何
術曰置粟數二十一升以粺米率二十七乘之得五百六十七升為實以粟率五十為法除之不盡以法而命分
答曰 a斗 
"""

"""
Suppose there are 2 dou and 1 sheng of unhusked millet.
Question: how much polished rice does it make?

The procedure says: Place the amount of millet, 21 sheng.
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

# 以粟數乘粺米率，得實
實 = 粟 * 粺米率

# 以粟率為法除之
a = Fraction(實, 粟率) / 10  # Convert back to dou (1 dou = 10 sheng)
"""
"""
