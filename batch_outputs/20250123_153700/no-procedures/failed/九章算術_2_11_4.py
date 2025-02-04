"""
今有粟四斗一升、太半升，欲為答。問︰得幾何？
荅曰：為答 a斗 。
"""

"""
Suppose there is 4 dou, 1 sheng, and half a sheng of millet. It is desired to turn it into da (a processed form of millet).
Question: how much da is obtained?

Answer: it makes *a* dou of da.
"""

from fractions import Fraction

# 粟四斗一升、太半升
粟 = 4 + Fraction(1, 10) + Fraction(1, 20)

# To convert millet into da, multiply by 2/3
a = 粟 * Fraction(2, 3)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 83/30"""
