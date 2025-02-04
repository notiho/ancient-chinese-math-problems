"""
今有粟七斗九升。問：為御米幾何？
答曰： a斗 。
"""

"""
Suppose there are 7 dou and 9 sheng of millet. It is desired to turn it into polished rice (御米).
Question: how much polished rice does it make?

Answer: it makes *a* dou.
"""

from fractions import Fraction

# 粟七斗九升
粟斗 = 7
粟升 = 9

# Convert everything to sheng (1 dou = 10 sheng)
總粟升 = 粟斗 * 10 + 粟升

# Polished rice is 50% of the original millet
御米升 = Fraction(總粟升, 2)

# Convert polished rice back to dou and sheng
a斗 = 御米升 // 10  # Whole dou
a升 = 御米升 % 10   # Remaining sheng

# Final result
a = Fraction(a斗) + Fraction(a升, 10)  # Represent as dou with fractional part

a
"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 79/20"""
