"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 2 dou and 3 sheng of millet. It is desired to turn it into roughly husked rice.
Question: how much roughly husked rice does it make?

The procedure says: when seeking roughly husked rice from millet, multiply by 3 and divide by 2.

The answer says: it makes *a* dou of roughly husked rice.
"""

from fractions import Fraction

# 粟二斗三升
粟斗 = 2  # 斗
粟升 = 3  # 升

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求糲飯，三之
糲飯升 = 3 * 粟總升

# 二而一
糲飯升 = Fraction(糲飯升, 2)

# Convert back to 斗 and 升
糲飯斗 = 糲飯升 // 10  # Whole number of dou
糲飯剩餘升 = 糲飯升 % 10  # Remaining sheng

# Final answer
a = Fraction(糲飯升, 10)  # Represent the result in dou
糲飯斗, 糲飯剩餘升#----- content ends here -----

"""
"""
