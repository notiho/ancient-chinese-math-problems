"""
今有粟四斗五升問為糳米幾何
術曰置粟四十五升以二約糳米率二十四得一十二乘之得五百四十升為實以二約粟率五十得二十五為法除之不盡以等數約之而命分
答曰 a斗 
"""

"""
Suppose there are 4 dou and 5 sheng of millet.
Question: how much roughly husked millet (糳米) does it make?

The procedure says: Place the millet as 45 sheng.
Divide by 2, obtaining the 糳米 rate of 24, and multiply by 12, obtaining 540 sheng as the dividend.
Divide by 2, obtaining the millet rate of 50, and divide by 25 as the divisor.
If the division is not exact, simplify the fraction and express it as a proper fraction.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟 = 粟斗 * 10 + 粟升  # Convert to sheng (1 dou = 10 sheng)

# 置粟四十五升
粟 = 45

# 以二約糳米率二十四
糳米率 = Fraction(24, 2)

# 得一十二乘之，得五百四十升為實
實 = 12 * 糳米率 * 粟

# 以二約粟率五十
粟率 = Fraction(50, 2)

# 得二十五為法
法 = 25

# 除之，不盡以等數約之而命分
a = Fraction(實, 法) / 10  # Convert back to dou (1 dou = 10 sheng)
"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 648/25"""
