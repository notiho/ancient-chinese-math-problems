"""
今有粟七斗九升，欲為御米。問︰得幾何？
荅曰：為御米 a斗 。
"""

"""
Suppose there are 7 dou and 9 sheng of millet. It is desired to turn it into polished rice (御米).
Question: how much polished rice does one obtain?

Answer: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟七斗九升
粟_斗 = 7
粟_升 = 9

# Convert everything to sheng (1 dou = 10 sheng)
total_升 = 粟_斗 * 10 + 粟_升

# Polished rice is obtained by multiplying the total millet by 2/3
御米_升 = Fraction(2, 3) * total_升

# Convert back to dou and sheng
御米_斗 = 御米_升 // 10  # Whole number of dou
御米_剩餘升 = 御米_升 % 10  # Remaining sheng

# Final result
a = Fraction(御米_升, 10)  # Express the result in dou

a
"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 79/15"""
