"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou and 5 sheng of millet. 
Question: how much roughly husked millet does it make?

The procedure says: Place 45 sheng of millet.
Divide by 2, giving the rate for roughly husked millet as 24.
Multiply by 12, obtaining 540 sheng as the dividend.
Divide by 2, giving the rate for millet as 25, which becomes the divisor.
Perform the division. If there is a remainder, reduce it with a common factor and assign the fraction.

Answer: it makes *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟總升 = 粟斗 * 10 + 粟升  # 1斗 = 10升

# 粟率置四十五升
粟率 = 45

# 以二約糳米率二十四，得一十二
糳米率 = Fraction(24, 2)

# 乘之，得五百四十升，為實
實 = 粟總升 * 糳米率

# 以二約粟率，五十得二十五，為法
法 = Fraction(50, 2)

# 除之，不盡，以等數約之，而命分
a = Fraction(實, 法) / 10  # Convert back to dou (1斗 = 10升)#----- content ends here -----

"""
"""
