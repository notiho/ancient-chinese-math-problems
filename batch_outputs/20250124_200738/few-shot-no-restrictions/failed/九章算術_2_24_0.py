"""
今有糲米一十九斗二升、七分升之一，欲為粺米。問︰得幾何？
術曰：以糲米求粺米，九之，十而一。
荅曰：為粺米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 19 dou, 2 sheng, and 1/7 of a sheng of roughly husked millet (糲米). 
It is desired to turn it into finely husked millet (粺米).
Question: how much does one obtain?

The procedure says: when seeking finely husked millet using roughly husked millet, multiply by 9 and divide by 10.

Answer: it makes *a* dou of finely husked millet.
"""

from fractions import Fraction

# 糲米一十九斗二升、七分升之一
糲米 = 19 + Fraction(2, 10) + Fraction(1, 7 * 10)

# 以糲米求粺米，九之
粺米 = 9 * 糲米

# 十而一
粺米 = Fraction(粺米, 10)

# Convert result to dou and sheng
斗 = int(粺米)  # Whole number part is in dou
升 = (粺米 - 斗) * 10  # Remaining part is in sheng

a = f"{斗}斗 {升}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2421/140, Actual: 17斗 41/14升"""
