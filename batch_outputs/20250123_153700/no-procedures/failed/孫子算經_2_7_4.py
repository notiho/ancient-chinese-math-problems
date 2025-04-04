"""
今有粟七斗九升。問：為御米幾何？
答曰： a斗 。
"""

"""
Suppose there is 7 dou and 9 sheng of millet. It is desired to turn it into polished rice (御米).
Question: how much polished rice does it make?

Answer: it makes *a* dou.
"""

from fractions import Fraction

# 粟七斗九升
粟_斗 = 7
粟_升 = 9

# Convert everything to sheng (1 dou = 10 sheng)
粟_總升 = 粟_斗 * 10 + 粟_升

# Polished rice is 50% of the millet
御米_總升 = Fraction(粟_總升, 2)

# Convert back to dou and sheng
a_斗 = 御米_總升 // 10  # Whole dou
a_升 = 御米_總升 % 10   # Remaining sheng

# Final result
a = Fraction(a_斗) + Fraction(a_升, 10)  # Express as dou

a  # Output the result in dou
"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 79/20"""
