"""
今有粟二斗一升，欲為粺米。問︰得幾何？
荅曰：為粺米 a斗 。
"""

"""
Suppose there is 2 dou and 1 sheng of unhusked millet. It is desired to turn it into polished millet.
Question: how much polished millet does one obtain?

The answer says: it makes *a* dou.
"""

from fractions import Fraction

# 粟二斗一升
粟 = 2 + Fraction(1, 10)  # 1 dou = 10 sheng, so 1 sheng = 1/10 dou

# Conversion ratio for polished millet: 1 dou of unhusked millet yields 1/2 dou of polished millet
a = Fraction(1, 2) * 粟  # Multiply by the conversion ratio

# Result
a
"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 21/20"""
