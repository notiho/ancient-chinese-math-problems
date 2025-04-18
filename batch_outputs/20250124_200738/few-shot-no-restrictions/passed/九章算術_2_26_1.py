"""
今有糲飯七斗六升、七分升之四，欲為飧。問︰得幾何？
術曰：以糲飯求飧，六之，五而一。
荅曰：為飧 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 7 dou, 6 sheng, and 4/7 of a sheng of roughly husked rice. It is desired to turn it into cooked rice (飧).
Question: how much cooked rice does it make?

The procedure says: When seeking cooked rice using roughly husked rice, multiply by 6 and divide by 5.

Answer: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 糲飯七斗六升、七分升之四
糲飯 = 7 + Fraction(6, 10) + Fraction(4, 70)  # Convert everything to dou (1 dou = 10 sheng)

# 以糲飯求飧，六之
飧 = 6 * 糲飯

# 五而一
a = Fraction(飧, 5)

# Output the result
a#----- content ends here -----

"""
"""
