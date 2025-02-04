"""
今有糲米一十九斗二升、七分升之一，欲為粺米。問︰得幾何？
術曰：以糲米求粺米，九之，十而一。
荅曰：為粺米 a斗 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 糲米一十九斗二升、七分升之一
糲米 = 19 + Fraction(2, 10) + Fraction(1, 70)

# 以糲米求粺米，九之
粺米 = 9 * 糲米

# 十而一
a = Fraction(粺米, 10)
#----- content ends here -----


"""

"""


"""
"""
