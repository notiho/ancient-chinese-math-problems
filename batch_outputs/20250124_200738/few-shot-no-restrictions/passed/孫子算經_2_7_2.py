"""
今有粟七斗九升。問：為御米幾何？
術曰：置七斗九升以御米率二十一乘之，得一千六百五十九，為實，以粟率五十除之，即得。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 9 sheng of millet. 
Question: how much polished rice does it make?

The procedure says: Take 7 dou and 9 sheng, multiply it by the polished rice rate of 21, obtaining 1659 as the dividend.
Divide it by the millet rate of 50, obtaining the result.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟七斗九升
粟斗 = 7
粟升 = 9

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 御米率二十一
御米率 = 21

# 粟率五十
粟率 = 50

# Multiply by 御米率 to get the dividend
實 = 粟總升 * 御米率

# Divide by 粟率 to get the result
a = Fraction(實, 粟率) / 10  # Convert back to dou

a#----- content ends here -----

"""
"""
