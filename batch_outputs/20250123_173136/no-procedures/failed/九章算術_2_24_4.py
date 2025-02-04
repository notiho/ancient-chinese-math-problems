"""
今有糲米一十九斗二升、七分升之一，欲為粺米。問︰得幾何？
荅曰：為粺米 a斗 。
"""

"""
Suppose there are 19 dou, 2 sheng, and 1/7 of a sheng of roughly husked millet (糲米). It is desired to turn it into finely husked millet (粺米).
Question: how much finely husked millet is obtained?

Answer: it makes *a* dou of finely husked millet.
"""

from fractions import Fraction

# 糲米 quantity: 19 dou, 2 sheng, and 1/7 of a sheng
糲米 = 19 + Fraction(2, 10) + Fraction(1, 70)  # Convert everything to dou (1 dou = 10 sheng)

# Conversion rate: 粺米 is 4/5 of 糲米
a = Fraction(4, 5) * 糲米

# Result
a
"""
Variable 'a' has wrong value. Expected: 2421/140, Actual: 538/35"""
