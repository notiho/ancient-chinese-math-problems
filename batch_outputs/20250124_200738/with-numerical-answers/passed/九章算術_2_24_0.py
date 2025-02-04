"""
今有糲米一十九斗二升、七分升之一，欲為粺米。問︰得幾何？
術曰：以糲米求粺米，九之，十而一。
荅曰：為粺米 a(=2421/140)斗 。
"""

#----- content starts here -----
"""
Suppose there are 19 dou, 2 sheng, and 1/7 of a sheng of roughly husked millet. It is desired to turn it into finely husked millet.
Question: how much does one obtain?

The procedure says: when seeking finely husked millet with roughly husked millet, multiply by 9 and divide by 10.

The answer says: *a*(=2421/140) dou of finely husked millet.
"""

from fractions import Fraction

# 糲米一十九斗二升、七分升之一
糲米 = 19 + Fraction(2, 10) + Fraction(1, 70)  # Convert to dou (1 dou = 10 sheng)

# 以糲米求粺米，九之
粺米 = 9 * 糲米

# 十而一
a = Fraction(粺米, 10)  # 2421/140 dou#----- content ends here -----

"""
"""
