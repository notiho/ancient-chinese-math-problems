"""
今有粟二斗一升。問：為粺米幾何？
術曰：置粟數二十一升，以粺米率二十七乘之，得五百六十七升，為實；以粟率五十為法，除之不盡，以法而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 1 sheng of unhusked millet.
Question: how much polished millet does it make?

The procedure says: Place the number of millet, 21 sheng.
Multiply it by the polished millet rate, 27, obtaining 567 sheng as the dividend.
Use the millet rate, 50, as the divisor.
Divide, and if there is a remainder, express it as a fraction using the divisor.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟二斗一升
粟 = 2 * 10 + 1  # Convert to sheng (1 dou = 10 sheng)

# 粺米率二十七
粺米率 = 27

# 粟率五十
粟率 = 50

# 以粺米率二十七乘之，得實
實 = 粟 * 粺米率

# 以粟率五十為法，除之不盡，以法而命分
a = Fraction(實, 粟率)

# Convert result to dou and sheng
斗 = a.numerator // (10 * a.denominator)
升 = (a.numerator % (10 * a.denominator)) / a.denominator

print(f"{斗}斗 {升}升")#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 567/50"""
