"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
荅曰：為麻 a斗 。
"""

"""
Suppose there are 5 dou and 0.5 sheng of millet. It is desired to turn it into hemp.
Question: how much hemp does one obtain?

Answer: it makes *a* dou of hemp.
"""

from fractions import Fraction

# 粟五斗、太半升
粟 = 5 + Fraction(1, 2)  # 5 dou and 0.5 sheng

# Conversion ratio: millet to hemp is 3:10
a = Fraction(3 * 粟, 10)  # Convert millet to hemp

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 33/20"""
