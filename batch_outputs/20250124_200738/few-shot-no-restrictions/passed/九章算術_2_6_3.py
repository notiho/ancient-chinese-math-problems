"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 2 dou and 3 sheng of millet. It is desired to turn it into roughly husked rice.
Question: how much roughly husked rice does it make?

The procedure says: When seeking roughly husked rice from millet, multiply by 3 and divide by 2.

Answer: it makes *a* dou of roughly husked rice.
"""

from fractions import Fraction

# 粟二斗三升
粟斗 = 2
粟升 = 3

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求糲飯，三之
糲飯升 = 3 * 粟總升

# 二而一
糲飯總升 = Fraction(糲飯升, 2)

# Convert back to dou and sheng
糲飯斗 = 糲飯總升 // 10  # Whole dou
糲飯升 = 糲飯總升 % 10   # Remaining sheng

a = Fraction(糲飯斗) + Fraction(糲飯升, 10)  # Final result in dou
#----- content ends here -----

"""
"""
