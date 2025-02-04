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

# 以粺米率二十七乘之，得五百六十七升為實
實 = 粟 * 粺米率

# 粟率五十為法
法 = 50

# 以法除之，不盡以法而命分
a = Fraction(實, 法)  # Result in dou (1 dou = 10 sheng)

# Convert to dou and sheng for clarity
dou = a.numerator // a.denominator  # Whole dou
sheng = a.numerator % a.denominator  # Remaining sheng as fraction of dou
a = f"{dou} dou and {Fraction(sheng, a.denominator)} dou"  # Final answer in dou format
"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 11 dou and 17/50 dou"""
