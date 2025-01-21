"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

"""
Suppose person A (甲) has 3 sheng of millet (粟), person B (乙) has 3 sheng of roughly husked millet (糲米), and person C (丙) has 3 sheng of cooked millet rice (糲飯). 
They want to combine their contributions and divide them equally. 
Question: how much does each person get?

Answer: A gets *a* sheng, B gets *b* sheng, and C gets *c* sheng.
"""

# Conversion ratios:
# 1 sheng of millet (粟) produces 3/5 sheng of husked millet (糲米)
# 1 sheng of husked millet (糲米) produces 1/2 sheng of cooked millet rice (糲飯)

# Contributions in terms of cooked millet rice (糲飯):
甲_contribution = 3 * Fraction(3, 5) * Fraction(1, 2)  # Convert millet to cooked rice
乙_contribution = 3 * Fraction(1, 2)  # Convert husked millet to cooked rice
丙_contribution = 3  # Already in cooked rice form

# Total contribution in cooked rice:
total_cooked_rice = 甲_contribution + 乙_contribution + 丙_contribution

# Equal share for each person:
equal_share = total_cooked_rice / 3

# Convert equal share back to original forms:
# For A (甲), convert cooked rice back to millet:
a = equal_share / (Fraction(3, 5) * Fraction(1, 2))

# For B (乙), convert cooked rice back to husked millet:
b = equal_share / Fraction(1, 2)

# For C (丙), already in cooked rice form:
c = equal_share

# Results:
a, b, c
"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 6
Variable 'b' has wrong value. Expected: 9/2, Actual: 18/5"""
