"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is 4 dou and 5 sheng of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much does one obtain?

The procedure says: Place 45 sheng of millet. Divide by 2, using the millet-to-roughly-husked-millet ratio of 24, obtaining 12. Multiply it, obtaining 540 sheng as the dividend.
Divide by 2, using the millet ratio of 50, obtaining 25 as the divisor. Perform the division. If there is a remainder, reduce it using common factors and express it as a fraction.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟總升 = 粟斗 * 10 + 粟升  # 1斗 = 10升

# 粟率
粟率 = 50

# 糳米率
糳米率 = 24

# 置粟四十五升，以二約糳米率二十四，得一十二，乘之
實 = Fraction(粟總升 * 糳米率, 粟率)

# 轉換為斗和升
a斗 = 实 // 10  # 每10升為1斗
a升 = 实 % 10  # 剩餘升數

a = f"{a斗}斗 {a升}升"
#----- content ends here -----

"""
Code error: name '实' is not defined"""
