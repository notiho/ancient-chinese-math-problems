"""
今有粟九斗八升，欲為御飯。問︰得幾何？
荅曰：為御飯 a斗 。
"""

"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

Answer: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 粟九斗八升
粟_斗 = 9
粟_升 = 8

# Convert everything to sheng (1 dou = 10 sheng)
粟_總升 = 粟_斗 * 10 + 粟_升

# To make cooked rice, millet is reduced by 2/3 of its volume
御飯_總升 = Fraction(粟_總升 * 2, 3)

# Convert back to dou and sheng
a_斗 = 御飯_總升 // 10  # Whole dou
a_升 = 御飯_總升 % 10   # Remaining sheng

# Final result
a = Fraction(a_斗) + Fraction(a_升, 10)  # Represent as a single fraction in dou

a
"""
Variable 'a' has wrong value. Expected: 1029/125, Actual: 98/15"""
