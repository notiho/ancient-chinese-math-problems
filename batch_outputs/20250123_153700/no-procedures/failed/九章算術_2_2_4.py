"""
今有粟四斗五升，欲為鑿米。問︰得幾何？
荅曰：為鑿米 a斗 。
"""

"""
Suppose there are 4 dou and 5 sheng of unhusked millet. It is desired to turn it into polished (refined) rice.
Question: how much polished rice does one obtain?

Answer: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟四斗五升
粟_斗 = 4
粟_升 = 5

# Convert everything to sheng (1 dou = 10 sheng)
總粟_升 = 粟_斗 * 10 + 粟_升

# Polished rice is obtained by multiplying by 2/3
總鑿米_升 = Fraction(2, 3) * 總粟_升

# Convert back to dou and sheng
a_斗 = 總鑿米_升 // 10  # Whole dou
a_升 = 總鑿米_升 % 10   # Remaining sheng

# Final result
a = Fraction(a_斗) + Fraction(a_升, 10)
a
"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 3"""
