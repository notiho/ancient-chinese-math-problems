"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

"""
Suppose person A (甲) has 3 sheng of millet (粟), person B (乙) has 3 sheng of roughly husked millet (糲米), and person C (丙) has 3 sheng of cooked millet rice (糲飯). 
They want to combine their contributions and redistribute them equally. 
Question: how much does each person receive?

Answer: A receives *a* sheng, B receives *b* sheng, and C receives *c* sheng.
"""

# Conversion ratios:
# 1 sheng of millet (粟) = 3/5 sheng of husked millet (糲米)
# 1 sheng of husked millet (糲米) = 1/2 sheng of cooked millet rice (糲飯)

# Contributions in terms of cooked millet rice (糲飯):
甲_contribution = Fraction(3, 1) * Fraction(3, 5) * Fraction(1, 2)  # Convert 粟 -> 糲米 -> 糲飯
乙_contribution = Fraction(3, 1) * Fraction(1, 2)  # Convert 糲米 -> 糲飯
丙_contribution = Fraction(3, 1)  # Already in 糲飯

# Total contribution in 糲飯:
total_contribution = 甲_contribution + 乙_contribution + 丙_contribution

# Equal share for each person:
equal_share = total_contribution / 3

# Convert the equal share back to each person's original unit:
a = equal_share / (Fraction(3, 5) * Fraction(1, 2))  # 糲飯 -> 糲米 -> 粟
b = equal_share / Fraction(1, 2)  # 糲飯 -> 糲米
c = equal_share  # Already in 糲飯

a, b, c  # Results for 甲, 乙, 丙 respectively
"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 6
Variable 'b' has wrong value. Expected: 9/2, Actual: 18/5"""
