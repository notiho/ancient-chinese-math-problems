"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a(=54/25)斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou and 5 sheng of unhusked millet.
Question: how much roughly husked millet does it make?

The procedure says: Place 45 sheng of millet. Divide the millet rate of 24 by 2, obtaining 12, and multiply it, obtaining 540 sheng as the dividend.
Divide the millet rate of 50 by 2, obtaining 25 as the divisor.
Perform the division. If there is a remainder, reduce it with the common factor and express it as a fraction.

Answer: *a*(=54/25) dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟 = 粟斗 * 10 + 粟升  # Convert to sheng (1 dou = 10 sheng)

# 粟率二十四，糳米率五十
粟率 = 24
糳米率 = 50

# 以二約糳米率二十四，得一十二
糳米率 = 糳米率 // 2  # 25
粟率 = 粟率 // 2  # 12

# 乘之，得五百四十升，為實
實 = 粟 * 粟率  # 45 * 12 = 540

# 為法
法 = 糳米率  # 25

# 除之，不盡，以等數約之，而命分
a = Fraction(實, 法) /#----- content ends here -----

"""
Code error: invalid syntax (<string>, line 35)"""
