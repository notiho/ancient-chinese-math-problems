"""
今有粟四斗五升問為糳米幾何
術曰置粟四十五升以二約糳米率二十四得一十二乘之得五百四十升為實以二約粟率五十得二十五為法除之不盡以等數約之而命分
答曰 a斗 
"""

"""
Suppose there are 4 dou and 5 sheng of millet. It is desired to turn it into coarse rice.
Question: how much coarse rice does it make?

The procedure says: Place the millet as 45 sheng. 
Divide by 2, the coarse rice rate, where 24 gives 1, obtaining 12. Multiply it, obtaining 540 sheng as the dividend.
Divide by 2, the millet rate, where 50 gives 1, obtaining 25 as the divisor.
Perform the division. If there is a remainder, simplify it with a common factor and express it as a fraction.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟 = 10 * 粟斗 + 粟升  # Convert to sheng

# 置粟四十五升
粟 = 45

# 以二約糳米率二十四得一十二
糳米率 = Fraction(24, 12)

# 乘之得五百四十升為實
實 = 粟 * Fraction(12)

# 以二約粟率五十得二十五為法
粟率 = Fraction(50, 25)

# 除之不盡，以等數約之而命分
a = Fraction(實, 粟率)

# Convert result to dou and sheng
a斗 = a // 10  # Whole dou
a升 = a % 10   # Remaining sheng
a = f"{a斗}斗 {a升}升"  # Final answer in dou and sheng format
"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 27斗 0升"""
