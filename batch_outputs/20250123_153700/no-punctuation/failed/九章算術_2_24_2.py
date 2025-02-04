"""
今有糲米一十九斗二升七分升之一欲為粺米問得幾何
術曰以糲米求粺米九之十而一
荅曰為粺米 a斗 
"""

"""
Suppose there are 19 dou, 2 sheng, and 1/7 of a sheng of roughly husked millet (糲米).
It is desired to turn it into finely husked millet (粺米).
Question: how much does one obtain?

The procedure says: when seeking finely husked millet using roughly husked millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of finely husked millet.
"""

from fractions import Fraction

# 糲米一十九斗二升七分升之一
糲米 = 19 * 10 + 2 + Fraction(1, 7)  # Convert everything to sheng (1 dou = 10 sheng)

# 以糲米求粺米，九之
粺米 = 9 * 糲米

# 十而一
粺米 = Fraction(粺米, 10)

# Convert back to dou and sheng
粺米斗 = int(粺米 // 10)  # Whole dou
粺米升 = 粺米 % 10  # Remaining sheng

a = (粺米斗, 粺米升)  # Answer in (dou, sheng) format
"""
Variable 'a' has wrong value. Expected: 2421/140, Actual: (17, Fraction(41, 14))"""
