"""
今有粟二斗一升。問：為粺米幾何？
術曰：置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實；以粟率五十為法，除之不盡，以法而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 1 sheng of millet. 
Question: how much polished rice does it make?

The procedure says: Place the millet quantity, 21 sheng, and multiply it by the polished rice rate, 27, obtaining 567 sheng as the dividend.
Take the millet rate, 50, as the divisor, and divide. If there is a remainder, express it as a fraction of the divisor.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟二斗一升
粟斗 = 2
粟升 = 1
# Convert to total sheng (1 dou = 10 sheng)
粟數 = 粟斗 * 10 + 粟升

# 粺米率二十七
粺米率 = 27

# 粟率五十
粟率 = 50

# Multiply millet quantity by polished rice rate
實 = 粟數 * 粺米率

# Divide by millet rate
a = Fraction(實, 粟率)

# Convert result to dou and sheng
a斗 = a.numerator // 10
a升 = a.numerator % 10
a = f"{a斗}斗 {Fraction(a升, a.denominator)}升"

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 56斗 7/50升"""
