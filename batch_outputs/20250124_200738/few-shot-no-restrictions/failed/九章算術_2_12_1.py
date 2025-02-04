"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 0.5 sheng of millet. It is desired to convert it into hemp (ma).
Question: how much hemp does it make?

The procedure says: When seeking beans (shu), da, hemp (ma), or wheat (mai) from millet, multiply by 9 and divide by 10.

Answer: it makes *a* dou of hemp.
"""

from fractions import Fraction

# 粟五斗、太半升
粟斗 = 5
粟升 = Fraction(1, 2)  # 太半升 = 0.5升

# Convert everything to 升 (1斗 = 10升)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求麻，皆九之，十而一
麻升 = Fraction(9, 10) * 粟總升

# Convert back to 斗 (1斗 = 10升)
麻斗 = 麻升 / 10

# Answer
a = 麻斗
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/200"""
