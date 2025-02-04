"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is 4 dou and 5 sheng of millet. 
Question: how much roughly husked millet (糳米) does it make?

The procedure says: Place the millet as 45 sheng. 
Divide the 糳米 rate (24) by 2, obtaining 12, and multiply it by the millet, obtaining 540 sheng as the dividend.
Divide the millet rate (50) by 2, obtaining 25 as the divisor.
Perform the division. If there is a remainder, simplify it using the greatest common divisor, and express it as a fraction.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟 = 粟斗 * 10 + 粟升  # Convert everything to sheng (1 dou = 10 sheng)

# 糳米率 and 粟率
糳米率 = 24
粟率 = 50

# Divide 糳米率 and 粟率 by 2
糳米率 = 糳米率 // 2
粟率 = 粟率 // 2

# Calculate the dividend (實)
實 = 糳米率 * 粟

# Calculate the divisor (法)
法 = 粟率

# Perform the division
a = Fraction(實, 法)

# Convert the result to dou and sheng
a斗 = a.numerator // a.denominator // 10  # Whole dou
a升 = (a.numerator // a.denominator) % 10  # Remaining sheng
a分 = Fraction(a.numerator % a.denominator, a.denominator)  # Fractional part

# Final answer
a斗, a升, a分#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 108/5"""
