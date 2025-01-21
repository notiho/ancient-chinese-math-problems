"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a(=54/25)斗 。
"""

"""
Suppose there are 4 dou and 5 sheng of unhusked millet.
Question: how much roughly husked millet does it make?

The procedure says: Place 45 sheng of unhusked millet. Divide by 2 the rate for roughly husked millet, which is 24, obtaining 12. Multiply by it, obtaining 540 sheng as the dividend. Divide by 2 the rate for unhusked millet, which is 50, obtaining 25 as the divisor. Perform the division. If there is a remainder, simplify it using the greatest common divisor, and express the result as a fraction.

Answer: *a*(=54/25) dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5

# Convert to 升
粟 = 粟斗 * 10 + 粟升  # 4斗5升 = 45升

# 糳米率二十四
糳米率 = 24

# 以二約糳米率二十四，得一十二
糳米率 = 糳米率 // 2  # 12

# 乘之，得五百四十升，為實
實 = 粟 * 糳米率  # 45 * 12 = 540

# 粟率五十
粟率 = 50

# 以二約粟率五十，得二十五，為法
法 = 粟率 // 2  # 25

# 除之，不盡，以等數約之，而命分
a = Fraction(實, 法) / 10  # Convert back to dou: 540/25 = 54/25斗
"""
"""
