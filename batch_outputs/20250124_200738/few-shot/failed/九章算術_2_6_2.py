"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 3 sheng of unhusked millet. It is desired to turn it into roughly husked rice.
Question: how much roughly husked rice does it make?

The procedure says: When seeking roughly husked rice using unhusked millet, multiply by 3 and divide by 2.

The answer says: it makes *a* dou of roughly husked rice.
"""

from fractions import Fraction

# 粟二斗三升
粟斗 = 2
粟升 = 3

# Convert everything to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求糲飯，三之
糲飯 = 3 * 粟

# 二而一
糲飯 = Fraction(糲飯, 2)

# Convert back to 斗 and 升
a斗 = 糲飯 // 10  # Whole dou
a升 = 糲飯 % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"  # Final result in dou and sheng format#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 69/20, Actual: 3斗 9/2升"""
