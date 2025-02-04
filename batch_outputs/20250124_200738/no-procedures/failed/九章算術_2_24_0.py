"""
今有糲米一十九斗二升、七分升之一，欲為粺米。問︰得幾何？
荅曰：為粺米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 19 dou, 2 sheng, and 1/7 of a sheng of roughly husked millet (糲米). It is desired to turn it into finely husked millet (粺米).
Question: how much finely husked millet does one obtain?

Answer: it makes *a* dou.
"""

from fractions import Fraction

# 糲米 total in dou
糲米 = 19 + Fraction(2, 10) + Fraction(1, 70)  # 1 dou = 10 sheng, so 2 sheng = 2/10 dou, and 1/7 sheng = 1/70 dou

# Conversion ratio: finely husked millet (粺米) is 4/5 of roughly husked millet (糲米)
a = Fraction(4, 5) * 糲米

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2421/140, Actual: 538/35"""
