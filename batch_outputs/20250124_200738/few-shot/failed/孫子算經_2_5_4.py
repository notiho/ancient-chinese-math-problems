"""
今有粟二斗一升。問：為粺米幾何？
術曰：置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實；以粟率五十為法，除之不盡，以法而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 1 sheng of millet. 
Question: how much polished rice does it make?

The procedure says: Place the millet amount, 21 sheng. 
Multiply it by the polished rice rate, 27, obtaining 567 sheng as the dividend. 
Use the millet rate, 50, as the divisor. 
Divide, and if there is a remainder, express it as a fraction of the divisor.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟二斗一升
粟斗 = 2
粟升 = 1
粟數 = 粟斗 * 10 + 粟升  # Convert to sheng (1 dou = 10 sheng)

# 粺米率二十七
粺米率 = 27

# 粟率五十
粟率 = 50

# 置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實
實 = 粟數 * 粺米率

# 以粟率五十為法，除之不盡，以法而命分
a = Fraction(實, 粟率)

# Convert result to dou and sheng
a斗 = a.numerator // a.denominator // 10  # Whole dou
a升 = (a.numerator // a.denominator) % 10  # Remaining sheng
a分 = Fraction(a.numerator % a.denominator, a.denominator)  # Fractional part

a = f"{a斗}斗 {a升}升 {a分}斗" if a分 != 0 else f"{a斗}斗 {a升}升"
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 1斗 1升 17/50斗"""
