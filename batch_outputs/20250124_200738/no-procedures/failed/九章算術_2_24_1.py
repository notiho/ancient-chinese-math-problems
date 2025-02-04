"""
今有糲米一十九斗二升、七分升之一，欲為粺米。問︰得幾何？
荅曰：為粺米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 19 dou, 2 sheng, and 1/7 of a sheng of roughly husked millet (糲米). It is desired to turn it into finely husked millet (粺米).
Question: how much finely husked millet does one obtain?

Answer: it makes *a* dou of finely husked millet.
"""

# Import Fraction for fractional calculations
from fractions import Fraction

# 糲米 total: 19斗2升7分升之一
糲米 = 19 * 10 + 2 + Fraction(1, 7)  # Convert everything to sheng (1 dou = 10 sheng)

# Conversion ratio: 粺米 = 糲米 * 4 / 5
粺米 = 糲米 * Fraction(4, 5)

# Convert 粺米 back to dou
a = 粺米 / 10  # 1 dou = 10 sheng

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2421/140, Actual: 538/35"""
