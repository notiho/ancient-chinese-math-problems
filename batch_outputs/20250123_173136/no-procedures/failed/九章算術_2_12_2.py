"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
荅曰：為麻 a斗 。
"""

"""
Suppose there are 5 dou and half a sheng of millet. It is desired to turn it into hemp.
Question: how much hemp does one obtain?

Answer: it makes *a* dou of hemp.
"""

from fractions import Fraction

# 粟五斗、太半升
粟 = 5 + Fraction(1, 2)  # 5 dou and half a sheng

# Convert dou to sheng (1 dou = 10 sheng)
粟_in_sheng = 粟 * 10

# Conversion ratio: millet to hemp is 2/3
麻_in_sheng = Fraction(2, 3) * 粟_in_sheng

# Convert back to dou (1 dou = 10 sheng)
a = 麻_in_sheng / 10

# Result
a
"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 11/3"""
