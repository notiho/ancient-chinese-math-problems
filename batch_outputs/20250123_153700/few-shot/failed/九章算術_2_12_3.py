"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a斗 。
"""

"""
Suppose there are 5 dou and 0.5 sheng of millet. It is desired to convert it into hemp.
Question: how much hemp does it yield?

The procedure says: When seeking beans, peas, hemp, or wheat from millet, multiply by 9 and divide by 10.

The answer says: it yields *a* dou of hemp.
"""

from fractions import Fraction

# 粟五斗、太半升
粟斗 = 5
粟升 = Fraction(1, 2)

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求麻，皆九之
麻升 = 9 * 粟總升

# 十而一
麻斗 = Fraction(麻升, 10)

# Convert back to dou
a = 麻斗
"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/20"""
