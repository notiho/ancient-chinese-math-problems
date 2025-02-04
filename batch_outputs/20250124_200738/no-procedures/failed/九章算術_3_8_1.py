"""
今有甲持粟三升，乙持糲米三升，丙持糲飯三升。欲令合而分之，問︰各幾何？
荅曰：甲 a升 。乙 b升 。丙 c升 。
"""

#----- content starts here -----
"""
Suppose person A (甲) has 3 sheng of millet (粟), person B (乙) has 3 sheng of roughly husked millet (糲米), and person C (丙) has 3 sheng of cooked millet (糲飯). 
They want to combine their contributions and redistribute them equally. 
Question: how much does each person get?

Answer: A gets *a* sheng, B gets *b* sheng, and C gets *c* sheng.
"""

# Conversion rates:
# 1 sheng of millet (粟) = 3/5 sheng of husked millet (糲米)
# 1 sheng of husked millet (糲米) = 2/5 sheng of cooked millet (糲飯)

# Contributions in terms of cooked millet (糲飯):
甲_contribution = 3 * Fraction(3, 5) * Fraction(2, 5)  # Convert millet to cooked millet
乙_contribution = 3 * Fraction(2, 5)                  # Convert husked millet to cooked millet
丙_contribution = 3                                   # Already in cooked millet form

# Total cooked millet:
total_cooked_millet = 甲_contribution + 乙_contribution + 丙_contribution

# Redistribute equally:
equal_share = total_cooked_millet / 3

# Convert back to each person's original form:
a = equal_share / (Fraction(3, 5) * Fraction(2, 5))  # Convert cooked millet to millet
b = equal_share / Fraction(2, 5)                    # Convert cooked millet to husked millet
c = equal_share                                     # Already in cooked millet form

# Results:
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 27/10, Actual: 41/6
Variable 'b' has wrong value. Expected: 9/2, Actual: 41/10
Variable 'c' has wrong value. Expected: 9/5, Actual: 41/25"""
