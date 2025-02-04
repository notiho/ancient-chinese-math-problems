"""
今有粟四斗五升問為糳米幾何
術曰置粟四十五升以二約糳米率二十四得一十二乘之得五百四十升為實以二約粟率五十得二十五為法除之不盡以等數約之而命分
答曰 a斗 
"""

#----- content starts here -----
"""
Suppose there are 4 dou and 5 sheng of millet. Question: how much roughly husked millet (糳米) does it make?

The procedure says: Place the millet as 45 sheng. Divide by 2, the rate for roughly husked millet is 24, obtaining 12. Multiply it, obtaining 540 sheng as the dividend.
Divide by 2, the rate for millet is 50, obtaining 25 as the divisor.
Perform the division. If there is a remainder, simplify it using the common factor and express it as a fraction.

Answer: *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5

# 置粟四十五升
粟總升 = 粟斗 * 10 + 粟升  # 1斗 = 10升
assert 粟總升 == 45  # Confirming the total millet in sheng

# 以二約糳米率二十四得一十二
糳米率 = 24
糳米約分 = 2
糳米得 = Fraction(糳米率, 糳米約分)  # 得 12

# 乘之得五百四十升為實
實 = 粟總升 * 糳米得

# 以二約粟率五十得二十五為法
粟率 = 50
粟約分 = 2
法 = Fraction(粟率, 粟約分)  # 得 25

# 除之不盡以等數約之而命分
a = Fraction(實, 法)  # Perform the division and simplify

# Convert result to dou and sheng
a斗 = a.numerator // a.denominator // 10  # Whole dou
a升 = (a.numerator // a.denominator) % 10  # Remaining sheng
a分數 = Fraction(a.numerator % a.denominator, a.denominator)  # Fractional part if any

# Final result
a = f"{a斗}斗 {a升}升 {a分數}升" if a分數 != 0 else f"{a斗}斗 {a升}升"#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 2斗 1升 3/5升"""
