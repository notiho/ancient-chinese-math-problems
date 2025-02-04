"""
今有粟七斗九升問為御米幾何
術曰置七斗九升以御米率二十一乘之得一千六百五十九為實以粟率五十除之即得
答曰 a斗 
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 9 sheng of millet. 
Question: how much polished rice does it make?

The procedure says: Place the 7 dou and 9 sheng. 
Multiply it by the polished rice rate, 21, obtaining 1659 as the dividend. 
Divide it by the millet rate, 50, obtaining the result.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟七斗九升
粟斗 = 7
粟升 = 9
總粟升 = 粟斗 * 10 + 粟升  # Convert everything to sheng (1 dou = 10 sheng)

# 御米率二十一
御米率 = 21

# 粟率五十
粟率 = 50

# 以御米率二十一乘之，得實
實 = 總粟升 * 御米率

# 以粟率五十除之，即得
總御米升 = Fraction(實, 粟率)

# Convert back to dou and sheng
a斗 = 總御米升 // 10  # Whole dou
a升 = 總御米升 % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 3斗 159/50升"""
