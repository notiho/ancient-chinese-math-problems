"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou and 5 sheng of unhusked millet. 
Question: how much roughly husked millet (糳米) does it make?

The procedure says: Place the millet as 45 sheng. 
Divide the millet rate (粟率) of 24 by 2, obtaining 12. Multiply it, obtaining 540 sheng, as the dividend.
Divide the millet divisor (粟率) of 50 by 2, obtaining 25, as the divisor.
Perform the division. If there is a remainder, simplify it using the greatest common divisor, and express it as a fraction.

The answer says: *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5

# Convert 粟 to 升 (1 斗 = 10 升)
粟 = 粟斗 * 10 + 粟升

# 粟率
糳米率 = 24
粟率 = 50

# 以二約糳米率，得一十二
糳米率 = 糳米率 // 2

# 乘之，得五百四十升，為實
實 = 粟 * 糳米率

# 以二約粟率，得二十五，為法
法 = 粟率 // 2

# Perform the division
a = Fraction(實, 法)

# Convert result back to dou and sheng
a斗 = a.numerator // a.denominator // 10
a升 = a.numerator // a.denominator % 10
a = f"{a斗}斗 {a升}升"

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 2斗 1升"""
