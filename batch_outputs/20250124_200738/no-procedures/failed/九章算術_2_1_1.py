"""
今有粟二斗一升，欲為粺米。問︰得幾何？
荅曰：為粺米 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 2 dou and 1 sheng of unhusked millet. It is desired to turn it into polished millet.
Question: how much polished millet does one obtain?

The answer says: it makes *a* dou.
"""

from fractions import Fraction

# 粟二斗一升
粟 = 2 + Fraction(1, 10)  # 2 dou and 1 sheng (1 dou = 10 sheng)

# Conversion ratio: polished millet is 2/3 of unhusked millet
a = Fraction(2, 3) * 粟

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 7/5"""
