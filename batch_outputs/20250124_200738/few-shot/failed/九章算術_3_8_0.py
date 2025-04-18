"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

#----- content starts here -----
"""
Suppose person A holds 3 sheng of millet, person B holds 3 sheng of roughly husked millet, and person C holds 3 sheng of roughly cooked millet.
It is desired to combine and redistribute them equally.
Question: how much does each person receive?

The reverse-weighting procedure says: Place the weights in a line and let them multiply each other. The moving one becomes the weight of the unmoving one.
The procedure says: Use the millet rate of 50, the roughly husked millet rate of 30, and the roughly cooked millet rate of 75 as the weights, and reverse-weight them.
Add the auxiliary weights to form the divisor.
Multiply the total 9 sheng by the unreversed weights, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amount of 1 sheng.

Answer: A receives *a* sheng, B receives *b* sheng, and C receives *c* sheng.
"""

# 甲持粟三升
甲粟 = 3

# 乙持糲米三升
乙糲米 = 3

# 丙持糲飯三升
丙糲飯 = 3

# 粟率五十、糲米率三十、糲飯率七十五為衰
粟率 = 50
糲米率 = 30
糲飯率 = 75

# 返衰之
甲衰 = 粟率
乙衰 = 糲米率
丙衰 = 糲飯率

# 副并為法
法 = 甲衰 + 乙衰 + 丙衰

# 以九升乘未并者各自為實
總升 = 甲粟 + 乙糲米 + 丙糲飯
甲實 = 總升 * 甲衰
乙實 = 總升 * 乙衰
丙實 = 總升 * 丙衰

# 實如法得一升
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 90/31
Variable 'b' has wrong value. Expected: 9/2, Actual: 54/31
Variable 'c' has wrong value. Expected: 9/5, Actual: 135/31"""
