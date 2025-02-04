"""
今有甲持粟三升乙持糲米三升丙持糲飯三升欲令合而分之問各幾何
返衰術曰列置衰而令相乘動者為不動者衰術曰以粟率五十糲米率三十糲飯率七十五為衰而返衰之副并為法以九升乘未并者各自為實實如法得一升
荅曰甲 a升 乙 b升 丙 c升 
"""

#----- content starts here -----
"""
Suppose there are three people: Jia holds 3 sheng of millet, Yi holds 3 sheng of roughly husked millet, and Bing holds 3 sheng of roughly cooked millet.
It is desired to combine them and redistribute equally.
Question: how much does each person receive?

The "inverse weighting procedure" says: Place the weights in a line and let them multiply each other. The moving [quantity] becomes the stationary [quantity].
The "weighting procedure" says: Take the millet rate as 50, the roughly husked millet rate as 30, and the roughly cooked millet rate as 75 as the weights.
Reverse the weights, and add them together as the divisor.
Multiply the total 9 sheng by the unreversed weights, and each becomes its own dividend.
Divide by the divisor to obtain the amount for each person.

The answer says: Jia receives *a* sheng, Yi receives *b* sheng, and Bing receives *c* sheng.
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

# 合計九升
合計 = 甲粟 + 乙糲米 + 丙糲飯

# 以九升乘未并者各自為實
甲實 = 合計 * Fraction(1, 粟率)
乙實 = 合計 * Fraction(1, 糲米率)
丙實 = 合計 * Fraction(1, 糲飯率)

# 實如法得一升
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)#----- content ends here -----

"""
"""
