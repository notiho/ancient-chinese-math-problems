"""
今有粟二斗一升，欲為粺米。問︰得幾何？
術曰：以粟求粺米，二十七之，五十而一。
荅曰：為粺米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 1 sheng of unhusked millet. It is desired to turn it into polished millet.
Question: how much polished millet does one obtain?

The procedure says: when seeking polished millet from unhusked millet, multiply by 27 and divide by 50.

The answer says: it makes *a* dou of polished millet.
"""

from fractions import Fraction

# 粟二斗一升
粟_斗 = 2
粟_升 = 1

# Convert everything to 升 (1 斗 = 10 升)
粟 = 粟_斗 * 10 + 粟_升  # Total in 升

# 以粟求粺米，二十七之
粺米 = 27 * 粟

# 五十而一
粺米 = Fraction(粺米, 50)

# Convert back to 斗 (1 斗 = 10 升)
粺米_斗 = Fraction(粺米, 10)

a = 粺米_斗
#----- content ends here -----

"""
"""
