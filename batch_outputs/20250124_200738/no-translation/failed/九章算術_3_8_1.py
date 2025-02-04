"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

#----- content starts here -----

# 粟率五十、糲米率三十、糲飯率七十五為衰
粟率 = 50
糲米率 = 30
糲飯率 = 75

# 列置衰
衰 = [粟率, 糲米率, 糲飯率]

# 副并為法
法 = sum(衰)

# 以九升乘未并者各自為實
總量 = 9
實 = [總量 * rate for rate in 衰]

# 實如法得一升
甲 = Fraction(實[0], 法)
乙 = Fraction(實[1], 法)
丙 = Fraction(實[2], 法)

a = 甲
b = 乙
c = 丙#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 90/31
Variable 'b' has wrong value. Expected: 9/2, Actual: 54/31
Variable 'c' has wrong value. Expected: 9/5, Actual: 135/31"""
