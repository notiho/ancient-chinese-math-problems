"""
今有粟二斗一升問為粺米幾何
術曰置粟數二十一升以粺米率二十七乘之得五百六十七升為實以粟率五十為法除之不盡以法而命分
答曰 a斗 
"""

"""
Suppose there are 2 dou and 1 sheng of millet. Question: how much polished rice does it make?

The procedure says: Place the millet amount as 21 sheng. Multiply it by the polished rice rate, 27, obtaining 567 sheng as the dividend. Use the millet rate, 50, as the divisor. Divide it. If there is a remainder, express it as a fraction of the divisor.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟二斗一升
粟斗 = 2
粟升 = 1
# Convert to total sheng
粟數 = 10 * 粟斗 + 粟升

# 粺米率二十七
粺米率 = 27

# 以粺米率乘之，得五百六十七升為實
實 = 粟數 * 粺米率

# 粟率五十為法
法 = 50

# 以法除之，不盡以法而命分
a = Fraction(實, 法)

# Convert result to dou and sheng
a斗 = a.numerator // a.denominator // 10  # Whole dou
a升 = Fraction(a.numerator % (a.denominator * 10), a.denominator)  # Remaining sheng as a fraction

a = f"{a斗}斗 {a升}升"  # Final result in dou and sheng format
"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 1斗 67/50升"""
