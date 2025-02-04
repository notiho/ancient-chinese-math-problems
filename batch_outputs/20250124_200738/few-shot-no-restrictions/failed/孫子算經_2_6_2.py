"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou and 5 sheng of millet. 
Question: how much roughly husked millet (糳米) does it make?

The procedure says: Place 45 sheng of millet. Divide by 2, using the 糳米 rate of 24, obtaining 12. Multiply it, obtaining 540 sheng as the dividend.
Divide by 2, using the millet rate of 50, obtaining 25 as the divisor. Perform the division. If there is a remainder, simplify it using common factors, and express it as a fraction.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟總升 = 粟斗 * 10 + 粟升  # 1斗 = 10升

# 糳米率
糳米率 = 24

# 粟率
粟率 = 50

# 置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實
實 = Fraction(粟總升, 2) * Fraction(糳米率, 2)

# 以二約粟率，五十得二十五，為法
法 = Fraction(粟率, 2)

# 除之，不盡，以等數約之，而命分
糳米升 = Fraction(實, 法)

# Convert to dou and sheng
糳米斗 = 糳米升 // 10  # Whole dou
糳米剩餘升 = 糳米升 % 10  # Remaining sheng

a = f"{糳米斗}斗 {糳米剩餘升}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 1斗 4/5升"""
