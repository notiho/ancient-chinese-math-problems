"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a斗 。
"""

"""
Suppose there are 5 dou and half a sheng of millet. It is desired to convert it into hemp.
Question: how much hemp is obtained?

The procedure says: When seeking beans, peas, hemp, or wheat from millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of hemp.
"""

from fractions import Fraction

# 粟五斗、太半升
粟斗 = 5
粟升 = Fraction(1, 2)
# Convert everything to sheng (1 dou = 10 sheng)
粟 = 10 * 粟斗 + 粟升

# 皆九之
麻 = 9 * 粟

# 十而一
麻 = Fraction(麻, 10)

# Convert back to dou (1 dou = 10 sheng)
a = 麻 / 10  # Result in dou
"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/200"""
