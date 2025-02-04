"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a(=114/25)斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 1/2 sheng of millet. It is desired to convert it into hemp.
Question: how much hemp does it make?

The procedure says: When seeking beans, da, hemp, or wheat from millet, multiply by 9 and divide by 10.

Answer: it makes *a*(=114/25) dou of hemp.
"""

from fractions import Fraction

# 粟五斗、太半升
粟斗 = 5
粟升 = Fraction(1, 2)

# Convert 粟 to dou (1 dou = 10 sheng)
粟 = 10 * 粟斗 + 粟升  # Total in sheng

# 以粟求麻，皆九之
麻 = 9 * 粟

# 十而一
a = Fraction(麻, 10) / 10  # Convert back to dou (divide by 10 sheng per dou)

a = Fraction(114,25)#----- content ends here -----

"""
"""
