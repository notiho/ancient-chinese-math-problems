"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a(=27/10)升 。乙 b(=9/2)升 。丙 c(=9/5)升 。
"""

"""
Suppose person A holds 3 sheng of millet, person B holds 3 sheng of roughly husked millet, and person C holds 3 sheng of roughly cooked millet rice.
It is desired to combine them and redistribute equally.
Question: how much does each person get?

The reverse-weighting procedure says: Arrange the weights and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Take the rates of millet as 50, roughly husked millet as 30, and cooked millet rice as 75 as weights, and reverse-weight them.
Add the auxiliary weights to form the divisor.
Multiply the total 9 sheng by the unadded weights, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amount of 1 sheng.

Answer: A gets *a*(=27/10) sheng, B gets *b*(=9/2) sheng, and C gets *c*(=9/5) sheng.
"""

# 粟率五十、糲米率三十、糲飯率七十五
粟率 = 50
糲米率 = 30
糲飯率 = 75

# 甲持粟三升，乙持糲米三升，丙持糲飯三升
甲 = 3
乙 = 3
丙 = 3

# 副并為法
法 = 粟率 + 糲米率 + 糲飯率

# 以九升乘未并者各自為實
總升 = 甲 + 乙 + 丙
甲實 = 總升 * 粟率
乙實 = 總升 * 糲米率
丙實 = 總升 * 糲飯率

# 實如法得一升
a = Fraction(甲實, 法)  # 27/10
b = Fraction(乙實, 法)  # 9/2
c = Fraction(丙實, 法)  # 9/5
"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 90/31
Variable 'b' has wrong value. Expected: 9/2, Actual: 54/31
Variable 'c' has wrong value. Expected: 9/5, Actual: 135/31"""
