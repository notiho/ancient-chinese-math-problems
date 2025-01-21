"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a(=114/25)斗 。
"""

"""
Suppose there are 5 dou and half a sheng of millet. It is desired to convert it into hemp.
Question: how much hemp is obtained?

The procedure says: When seeking beans, da, hemp, or wheat from millet, multiply by 9 and divide by 10.

Answer: it makes *a*(=114/25) dou of hemp.
"""

from fractions import Fraction

# 粟五斗、太半升
粟斗 = 5
粟升 = Fraction(1, 2)  # 半升
粟 = 粟斗 + Fraction(粟升, 10)  # Convert sheng to dou (10 sheng = 1 dou)

# 以粟求麻，九之
麻 = 9 * 粟

# 十而一
a = Fraction(麻, 10)  # 114/25 dou
"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/200"""
