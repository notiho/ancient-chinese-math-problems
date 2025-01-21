"""
今有甲持粟三升乙持糲米三升丙持糲飯三升欲令合而分之問各幾何
返衰術曰列置衰而令相乘動者為不動者衰術曰以粟率五十糲米率三十糲飯率七十五為衰而返衰之副并為法以九升乘未并者各自為實實如法得一升
荅曰甲 a升 乙 b升 丙 c升 
"""

"""
Suppose there are three people: Jia holds 3 sheng of millet, Yi holds 3 sheng of roughly husked millet, and Bing holds 3 sheng of roughly cooked millet.
It is desired to combine and redistribute them equally.
Question: how much does each person receive?

The procedure for reverse proportional distribution says: Place the proportional rates in a line and let them multiply. The moving one becomes the stationary one.
The procedure says: Take the millet rate as 50, the roughly husked millet rate as 30, and the roughly cooked millet rate as 75 as the proportional rates.
Reverse the proportional rates, and their auxiliary sum becomes the divisor.
Multiply the total 9 sheng by the unreversed rates, and each becomes its own dividend.
Perform the division, obtaining the amount for one sheng.

The answer says: Jia gets *a* sheng, Yi gets *b* sheng, and Bing gets *c* sheng.
"""

# 甲持粟三升
甲粟 = 3

# 乙持糲米三升
乙糲米 = 3

# 丙持糲飯三升
丙糲飯 = 3

# 粟率五十
粟率 = 50

# 糲米率三十
糲米率 = 30

# 糲飯率七十五
糲飯率 = 75

# 返衰之副并為法
法 = Fraction(1, 粟率) + Fraction(1, 糲米率) + Fraction(1, 糲飯率)

# 以九升乘未并者
總升 = 甲粟 + 乙糲米 + 丙糲飯

# 各自為實
甲實 = 總升 * Fraction(1, 粟率)
乙實 = 總升 * Fraction(1, 糲米率)
丙實 = 總升 * Fraction(1, 糲飯率)

# 實如法得一升
a = 甲實 / 法
b = 乙實 / 法
c = 丙實 / 法
"""
"""
