"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a斗 。
"""

"""
Suppose there are 4 dou and 5 sheng of millet. 
Question: how much roughly husked millet (糳米) does it make?

The procedure says: Place 45 sheng of millet. Divide by 2, and use the 糳米 rate of 24, obtaining 12. Multiply this, obtaining 540 sheng as the dividend.
Divide by 2, and use the millet rate of 50, obtaining 25 as the divisor. Perform the division. If there is a remainder, reduce it with a common factor and express it as a fraction.

Answer: it makes *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟 = 4 * 10 + 5  # Convert to sheng (1 dou = 10 sheng)

# 粟率 50, 糳米率 24
粟率 = 50
糳米率 = 24

# 置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實
實 = Fraction(粟 * 糳米率, 粟率)

# 以二約粟率，五十得二十五，為法
法 = Fraction(粟率, 2)

# 除之，不盡，以等數約之，而命分
a = Fraction(實, 法) / 10  # Convert back to dou (1 dou = 10 sheng)
"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 54/625"""
