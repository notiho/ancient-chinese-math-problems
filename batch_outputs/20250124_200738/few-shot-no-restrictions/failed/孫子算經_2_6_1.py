"""
今有粟四斗五升。問：為糳米幾何？
術曰：置粟四十五升，以二約糳米率二十四，得一十二，乘之，得五百四十升，為實；以二約粟率，五十得二十五，為法，除之，不盡，以等數約之，而命分。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is 4 dou and 5 sheng of millet. 
Question: how much roughly husked millet (糳米) does it make?

The procedure says: Place 45 sheng of millet. Divide by 2, giving the 糳米 rate as 24, obtaining 12. Multiply it, obtaining 540 sheng as the dividend.
Divide by 2, giving the millet rate as 50, obtaining 25 as the divisor. Perform the division. If there is a remainder, simplify it using the greatest common divisor, and express it as a fraction.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5
粟總升 = 粟斗 * 10 + 粟升  # 1斗 = 10升

# 粟率與糳米率
粟率 = 50
糳米率 = 24

# 置粟四十五升，以二約糳米率二十四，得一十二
糳米基準 = 45
糳米基準約分 = 糳米基準 // 2
糳米基準得 = 糳米基準約分 // (糳米率 // 2)

# 乘之，得五百四十升，為實
實 = 粟總升 * 糳米基準得

# 以二約粟率，五十得二十五，為法
法 = 粟率 // 2

# 除之，不盡，以等數約之，而命分
糳米升 = Fraction(實, 法)

# 將升轉換為斗
a斗 = 糳米升 // 10  # 整斗數
a升 = 糳米升 % 10  # 剩餘升數

a = f"{a斗}斗 {a升}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 0斗 9/5升"""
