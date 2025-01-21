"""
今有粟七斗九升問為御米幾何
術曰置七斗九升以御米率二十一乘之得一千六百五十九為實以粟率五十除之即得
答曰 a斗 
"""

"""
Suppose there are 7 dou and 9 sheng of millet. 
Question: how much polished rice does it make?

The procedure says: Place 7 dou and 9 sheng. 
Multiply it by the polished rice rate, 21, obtaining 1659 as the dividend.
Divide it by the millet rate, 50, obtaining the result.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟七斗九升
粟斗 = 7
粟升 = 9

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = (粟斗 * 10) + 粟升

# 御米率二十一
御米率 = 21

# 以御米率二十一乘之，得實
實 = 粟總升 * 御米率

# 粟率五十
粟率 = 50

# 以粟率五十除之，即得
a = Fraction(實, 粟率) / 10  # Convert back to dou (1 斗 = 10 升)

a
"""
"""
