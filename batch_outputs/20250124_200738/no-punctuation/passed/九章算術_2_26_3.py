"""
今有糲飯七斗六升七分升之四欲為飧問得幾何
術曰以糲飯求飧六之五而一
荅曰為飧 a斗 
"""

#----- content starts here -----
"""
Suppose there is 7 dou, 6 sheng, and 4/7 of a sheng of roughly husked rice.
It is desired to turn it into cooked rice (suan).
Question: how much cooked rice does it make?

The procedure says: when seeking cooked rice using roughly husked rice, multiply by 6 and divide by 5.

The answer says: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 糲飯七斗六升七分升之四
糲飯 = 7 * 10 + 6 + Fraction(4, 7)  # Convert to sheng (1 dou = 10 sheng)

# 以糲飯求飧，六之
飧 = 6 * 糲飯

# 五而一
飧 = Fraction(飧, 5)

# Convert back to dou
a = Fraction(飧, 10)  # Convert sheng to dou (1 dou = 10 sheng)#----- content ends here -----

"""
"""
