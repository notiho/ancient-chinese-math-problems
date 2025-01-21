"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a(=54/25)斗 。
"""

"""
Suppose there are 4 dou and 5 sheng of unhusked millet. 
Question: how much roughly husked millet does it make?

The procedure says: Place 45 sheng of unhusked millet. Divide by 2, obtaining the roughly husked millet rate of 24, giving 12. Multiply it, obtaining 540 sheng as the dividend.
Divide by 2, obtaining the unhusked millet rate of 50, giving 25 as the divisor. Perform the division. If there is a remainder, simplify it using the common factor, and express it as a fraction.

Answer: *a*(=54/25) dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟 = 10 * 粟斗 + 粟升  # Convert to sheng (1 dou = 10 sheng)

# 粟率與糳米率
粟率 = 50
糳米率 = 24

# 置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實
實 = (粟 * Fraction(糳米率, 粟率))  # Calculate the roughly husked millet in sheng

# Convert result to dou (1 dou = 10 sheng)
a = Fraction(實, 10)  # 54/25 dou
"""
"""
