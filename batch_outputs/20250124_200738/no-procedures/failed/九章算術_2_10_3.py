"""
今有粟三斗少半升，欲為菽。問︰得幾何？
荅曰：為菽 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 3 dou and half a sheng of millet. It is desired to convert it into beans.
Question: how much does one obtain?

Answer: it makes *a* dou of beans.
"""

from fractions import Fraction

# 粟三斗少半升
粟 = 3 + Fraction(1, 20)  # 1 dou = 10 sheng, so half a sheng = 1/20 dou

# Conversion rate: millet to beans is 2/3
a = 粟 * Fraction(2, 3)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 273/100, Actual: 61/30"""
