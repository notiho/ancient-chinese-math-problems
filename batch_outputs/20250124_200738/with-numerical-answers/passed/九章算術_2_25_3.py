"""
今有糲米六斗四升、五分升之三，欲為糲飯。問︰得幾何？
術曰：以糲米求糲飯，五之，二而一。
荅曰：為糲飯 a(=323/20)斗 。
"""

#----- content starts here -----
"""
Suppose there are 6 dou, 4 sheng, and 3/5 of a sheng of roughly husked millet. It is desired to turn it into roughly husked rice.
Question: how much does one obtain?

The procedure says: when seeking roughly husked rice from roughly husked millet, multiply by 5 and divide by 2.

The answer says: it makes *a*(=323/20) dou of roughly husked rice.
"""

from fractions import Fraction

# 糲米六斗四升、五分升之三
糲米 = 6 + Fraction(4, 10) + Fraction(3, 50)  # Convert to dou (1 dou = 10 sheng)

# 以糲米求糲飯，五之
糲飯 = 5 * 糲米

# 二而一
a = Fraction(糲飯, 2)  # 323/20 dou#----- content ends here -----

"""
"""
