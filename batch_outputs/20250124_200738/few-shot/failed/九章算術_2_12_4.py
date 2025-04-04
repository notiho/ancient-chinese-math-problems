"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 dou and half a sheng of millet. It is desired to convert it into hemp.
Question: how much hemp is obtained?

The procedure says: When seeking beans, peas, hemp, or wheat from millet, multiply by 9 and divide by 10.

Answer: it makes *a* dou of hemp.
"""

from fractions import Fraction

# 粟五斗、太半升
粟斗 = 5
粟升 = Fraction(1, 2)

# Convert to total sheng (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求麻，皆九之
麻升 = 9 * 粟總升

# 十而一
麻斗 = Fraction(麻升, 10)

a = 麻斗#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/20"""
