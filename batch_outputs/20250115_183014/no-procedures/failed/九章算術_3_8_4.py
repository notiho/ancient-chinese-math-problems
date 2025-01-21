"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

"""
Suppose there are three people:
- Person A (甲) has 3 sheng of unhusked millet (粟),
- Person B (乙) has 3 sheng of roughly husked millet (糲米),
- Person C (丙) has 3 sheng of cooked millet (糲飯).

They want to combine their resources and redistribute them equally.  
Question: how much does each person get?

Answer: Person A gets *a* sheng, Person B gets *b* sheng, and Person C gets *c* sheng.
"""

from fractions import Fraction

# Conversion rates:
# 1 sheng of 粟 (unhusked millet) = 3/5 sheng of 糲米 (husked millet)
# 1 sheng of 糲米 (husked millet) = 2/5 sheng of 糲飯 (cooked millet)

# Initial contributions:
甲_粟 = 3  # 3 sheng of 粟
乙_糲米 = 3  # 3 sheng of 糲米
丙_糲飯 = 3  # 3 sheng of 糲飯

# Convert everything to 糲飯 (cooked millet):
甲_糲飯 = Fraction(甲_粟 * 3, 5) * Fraction(2, 5)  # Convert 粟 -> 糲米 -> 糲飯
乙_糲飯 = Fraction(乙_糲米 * 2, 5)  # Convert 糲米 -> 糲飯
丙_糲飯 = Fraction(丙_糲飯)  # Already in 糲飯

# Total amount of 糲飯:
總糲飯 = 甲_糲飯 + 乙_糲飯 + 丙_糲飯

# Divide equally among 3 people:
每人糲飯 = 總糲飯 / 3

# Convert back to each person's share:
# Person A (甲): 糲飯 -> 糲米 -> 粟
甲_粟分得 = 每人糲飯 * Fraction(5, 2) * Fraction(5, 3)

# Person B (乙): 糲飯 -> 糲米
乙_糲米分得 = 每人糲飯 * Fraction(5, 2)

# Person C (丙): 糲飯 remains the same
丙_糲飯分得 = 每人糲飯

# Final results:
a = 甲_粟分得
b = 乙_糲米分得
c = 丙_糲飯分得

a, b, c
"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 41/6
Variable 'b' has wrong value. Expected: 9/2, Actual: 41/10
Variable 'c' has wrong value. Expected: 9/5, Actual: 41/25"""
