"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
荅曰：為大䵂 a斗 。
"""

"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into coarse flour (大䵂).
Question: how much coarse flour is obtained?

Answer: it makes *a* dou of coarse flour.
"""

# 粟九斗八升
粟_斗 = 9
粟_升 = 8

# Convert everything to sheng (1 dou = 10 sheng)
total_粟_升 = 粟_斗 * 10 + 粟_升

# To make coarse flour, multiply by 7/10
total_大䵂_升 = Fraction(7 * total_粟_升, 10)

# Convert back to dou and sheng
a_斗 = total_大䵂_升 // 10  # Whole dou
a_升 = total_大䵂_升 % 10    # Remaining sheng

# Final result
a = Fraction(a_斗) + Fraction(a_升, 10)  # Represent as dou with fractional part
"""
Variable 'a' has wrong value. Expected: 1323/125, Actual: 343/50"""
