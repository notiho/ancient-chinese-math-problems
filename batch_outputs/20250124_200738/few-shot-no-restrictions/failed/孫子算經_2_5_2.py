"""
今有粟二斗一升。問：為粺米幾何？
術曰：置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實；以粟率五十為法，除之不盡，以法而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 1 sheng of unhusked millet. 
Question: how much polished rice does it yield?

The procedure says: Place the millet amount, 21 sheng, and multiply it by the polished rice rate, 27, obtaining 567 sheng as the dividend.
Take the millet rate, 50, as the divisor. Divide the dividend by the divisor. If there is a remainder, express it as a fraction of the divisor.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟二斗一升
粟斗 = 2
粟升 = 1
# Convert to total sheng (1 dou = 10 sheng)
粟數 = 10 * 粟斗 + 粟升

# 粺米率二十七
粺米率 = 27

# 以粺米率二十七乘之，得實
實 = 粟數 * 粺米率

# 粟率五十為法
法 = 50

# 除之不盡，以法而命分
a = Fraction(實, 法)

# Convert to dou and sheng
a斗 = a.numerator // a.denominator // 10  # Whole dou
a升 = (a.numerator // a.denominator) % 10  # Remaining sheng
a分 = Fraction(a.numerator % a.denominator, a.denominator)  # Fractional part

# Final answer
a斗, a升, a分#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 567/50"""
