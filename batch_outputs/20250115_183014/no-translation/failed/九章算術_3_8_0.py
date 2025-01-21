"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：以粟率五十、糲米率三十、糲飯率七十五為衰、而返衰之，副并為法。以九升乘未并者各自為實。實如法得一升。
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

"""

"""


from fractions import Fraction

# 粟率五十、糲米率三十、糲飯率七十五為衰
粟率 = 50
糲米率 = 30
糲飯率 = 75

# 列置衰而令相乘，動者為不動者衰
衰 = [粟率, 糲米率, 糲飯率]

# 副并為法
法 = sum(衰)

# 以九升乘未并者各自為實
總量 = 9
實 = [總量 * 粟率, 總量 * 糲米率, 總量 * 糲飯率]

# 實如法得一升
a, b, c = [Fraction(i, 法) for i in 實]

# 答案
print(f"甲 {a} 升。乙 {b} 升。丙 {c} 升。")


"""

"""


"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 90/31
Variable 'b' has wrong value. Expected: 9/2, Actual: 54/31
Variable 'c' has wrong value. Expected: 9/5, Actual: 135/31"""
