"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a(=27/10)升 。乙 b(=9/2)升 。丙 c(=9/5)升 。
"""

"""
Suppose Person A holds 3 sheng of millet, Person B holds 3 sheng of roughly husked millet, and Person C holds 3 sheng of roughly cooked millet.
It is desired to combine and redistribute them equally. 
Question: how much does each person receive?

The reverse weighting procedure says: Arrange the weights (rates) and let them multiply with each other. The moving one becomes the weight of the unmoving one.
The procedure says: Take the millet rate as 50, the roughly husked millet rate as 30, and the roughly cooked millet rate as 75 as the weights, and reverse them.
Add the auxiliary weights together to form the divisor.
Multiply the total 9 sheng by the unreversed weights, each becoming its own dividend.
Divide the dividends by the divisor to obtain the amount of 1 sheng for each person.

Answer: Person A receives *a*(=27/10) sheng, Person B receives *b*(=9/2) sheng, and Person C receives *c*(=9/5) sheng.
"""

# 粟率五十、糲米率三十、糲飯率七十五
粟率 = 50
糲米率 = 30
糲飯率 = 75

# 返衰之
粟返衰 = Fraction(1, 粟率)
糲米返衰 = Fraction(1, 糲米率)
糲飯返衰 = Fraction(1, 糲飯率)

# 副并為法
法 = 粟返衰 + 糲米返衰 + 糲飯返衰

# 以九升乘未并者各自為實
總量 = 9
粟實 = 總量 * 粟返衰
糲米實 = 總量 * 糲米返衰
糲飯實 = 總量 * 糲飯返衰

# 實如法得一升
a = Fraction(粟實, 法) # 27/10
b = Fraction(糲米實, 法) # 9/2
c = Fraction(糲飯實, 法) # 9/5
"""
"""
