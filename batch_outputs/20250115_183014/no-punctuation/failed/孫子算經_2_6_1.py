"""
今有粟四斗五升問為糳米幾何
術曰置粟四十五升以二約糳米率二十四得一十二乘之得五百四十升為實以二約粟率五十得二十五為法除之不盡以等數約之而命分
答曰 a斗 
"""

"""
Suppose there are 4 dou and 5 sheng of millet. 
Question: how much roughly husked millet (糳米) does it make?

The procedure says: Place the millet as 45 sheng. 
Divide by 2, the rate for roughly husked millet is 24, obtaining 12. Multiply it, obtaining 540 sheng as the dividend.
Divide by 2, the rate for millet is 50, obtaining 25 as the divisor.
Perform the division. If there is a remainder, simplify it with a common factor and express it as a fraction.

Answer: *a* dou.
"""

# 粟四斗五升
粟斗 = 4
粟升 = 5

# Convert to 升 (1 dou = 10 sheng)
粟 = 10 * 粟斗 + 粟升  # 粟 = 45 升

# 糳米率 24, divide by 2 to get 12
糳米率 = 24
糳米約 = 糳米率 // 2  # 糳米約 = 12

# Multiply to get the dividend (實)
實 = 糳米約 * 粟  # 實 = 540 升

# 粟率 50, divide by 2 to get 25
粟率 = 50
粟約 = 粟率 // 2  # 粟約 = 25

# Perform the division
a = Fraction(實, 粟約)  # a = 540 / 25

# Convert to dou and sheng
a斗 = a.numerator // a.denominator // 10  # Whole dou
a升 = (a.numerator // a.denominator) % 10  # Remaining sheng
a分 = Fraction(a.numerator % a.denominator, a.denominator)  # Fractional part if any

a = f"{a斗}斗 {a升}升 {a分} (if fractional part exists)"
"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 2斗 1升 3/5 (if fractional part exists)"""
