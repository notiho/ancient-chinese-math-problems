"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""


# 粟率、糲米率、糲飯率
粟率 = 50
糲米率 = 30
糲飯率 = 75

# 各持有量
甲持有 = 3
乙持有 = 3
丙持有 = 3

# 列置衰而令相乘，動者為不動者衰
甲衰 = 粟率
乙衰 = 糲米率
丙衰 = 糲飯率

# 副并為法
法 = (甲持有 * 甲衰) + (乙持有 * 乙衰) + (丙持有 * 丙衰)

# 以九升乘未并者各自為實
總量 = 9
甲實 = 總量 * 甲衰
乙實 = 総量 * 乙衰
丙實 = 總量 * 丙衰

# 實如法得一升
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)
"""
Code error: name '総量' is not defined"""
