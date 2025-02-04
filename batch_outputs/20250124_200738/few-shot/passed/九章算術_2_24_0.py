"""
今有糲米一十九斗二升、七分升之一，欲為粺米。問︰得幾何？
術曰：以糲米求粺米，九之，十而一。
荅曰：為粺米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 19 dou, 2 sheng, and 1/7 of a sheng of roughly husked millet (糲米). It is desired to turn it into finely husked millet (粺米).
Question: how much does one obtain?

The procedure says: when seeking finely husked millet using roughly husked millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of finely husked millet.
"""

from fractions import Fraction

# 糲米一十九斗二升、七分升之一
糲米 = 19 + Fraction(2, 10) + Fraction(1, 7 * 10)

# 以糲米求粺米，九之
粺米 = 9 * 糲米

# 十而一
a = Fraction(粺米, 10)  # 粺米 in dou#----- content ends here -----

"""
"""
