"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a(=54/25)斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou and 5 sheng of unhusked millet.
Question: how much roughly husked millet does it make?

The procedure says: Place 45 sheng of millet. Divide by 2, giving the rate for roughly husked millet as 24, obtaining 12. Multiply it, obtaining 540 sheng as the dividend.
Divide by 2, giving the rate for millet as 50, obtaining 25 as the divisor. Perform the division. If there is a remainder, simplify it using proportional numbers, and express it as a fraction.

Answer: *a*(=54/25) dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟 = 粟斗 * 10 + 粟升  # Convert to sheng (1 dou = 10 sheng)

# 粟率 50 (2約粟率，五十得二十五)
粟率 = 50
粟率約 = Fraction(粟率, 2)  # 25

# 糳米率 24 (2約糳米率，二十四得一十二)
糳米率 = 24
糳米率約 = Fraction(糳米率, 2)  # 12

# 置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實
實 = 粟 * 糳米率約  # 540

# 以二約粟率，五十得二十五，為法
法 = 粟率約  # 25

# 除之，不盡，以等數約之，而命分
a = Fraction(實, 法) / 10  # Convert back to dou (1 dou = 10 sheng)

# Answer
a  # 54/25 dou#----- content ends here -----

"""
"""
