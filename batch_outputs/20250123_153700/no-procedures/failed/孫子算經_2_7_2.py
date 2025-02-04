"""
今有粟七斗九升。問：為御米幾何？
答曰： a斗 。
"""

"""
Suppose there is 7 dou and 9 sheng of unhusked millet.
Question: how much polished rice (御米) does it make?

Answer: it makes *a* dou.
"""

from fractions import Fraction

# 粟七斗九升
粟_斗 = 7
粟_升 = 9

# Convert everything to sheng (1 dou = 10 sheng)
total_sheng = 粟_斗 * 10 + 粟_升

# Polished rice is 50% of unhusked millet
polished_rice_sheng = Fraction(total_sheng, 2)

# Convert polished rice back to dou and sheng
a_斗 = polished_rice_sheng // 10  # Whole dou
a_升 = polished_rice_sheng % 10   # Remaining sheng

# Final result
a = Fraction(a_斗) + Fraction(a_升, 10)  # Represent as dou

a  # Output the result as dou
"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 79/20"""
