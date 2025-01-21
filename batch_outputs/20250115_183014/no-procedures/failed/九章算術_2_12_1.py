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

# Conversion ratio: 1 dou of millet produces 3 dou of hemp
conversion_ratio = 3

# Calculate the amount of hemp
a = 粟 * conversion_ratio

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 33/2"""
