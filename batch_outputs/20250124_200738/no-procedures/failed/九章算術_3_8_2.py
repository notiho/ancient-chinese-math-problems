"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

#----- content starts here -----
"""
Suppose there are three people:
- Person A (甲) holds 3 sheng of millet (粟),
- Person B (乙) holds 3 sheng of roughly husked millet (糲米),
- Person C (丙) holds 3 sheng of cooked millet rice (糲飯).

They want to combine their holdings and divide them equally. 
Question: how much does each person get?

Answer: Person A gets *a* sheng, Person B gets *b* sheng, and Person C gets *c* sheng.
"""

# Conversion ratios:
# 1 sheng of 粟 (millet) = 3/5 sheng of 糲米 (husked millet)
# 1 sheng of 糲米 (husked millet) = 1/2 sheng of 糲飯 (cooked millet rice)

# Step 1: Convert everything to 糲飯 (cooked millet rice)
甲_in_糲飯 = Fraction(3, 1) * Fraction(3, 5) * Fraction(1, 2)  # 粟 -> 糲米 -> 糲飯
乙_in_糲飯 = Fraction(3, 1) * Fraction(1, 2)  # 糲米 -> 糲飯
丙_in_糲飯 = Fraction(3, 1)  # Already in 糲飯

# Total 糲飯
total_糲飯 = 甲_in_糲飯 + 乙_in_糲飯 + 丙_in_糲飯

# Step 2: Divide equally among the three people
equal_share_糲飯 = total_糲飯 / 3

# Step 3: Convert equal shares back to the original units for each person
# Person A (甲) gets:
a = equal_share_糲飯 * Fraction(2, 1) * Fraction(5, 3)  # 糲飯 -> 糲米 -> 粟

# Person B (乙) gets:
b = equal_share_糲飯 * Fraction(2, 1)  # 糲飯 -> 糲米

# Person C (丙) gets:
c = equal_share_糲飯  # Already in 糲飯

# Final results:
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 6
Variable 'b' has wrong value. Expected: 9/2, Actual: 18/5"""
