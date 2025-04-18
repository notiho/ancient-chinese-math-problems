"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a(=69/20)斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 3 sheng of unhusked millet. It is desired to turn it into roughly husked rice.
Question: how much does one obtain?

The procedure says: when seeking roughly husked rice with unhusked millet, multiply by 3 and divide by 2.

The answer says: *a*(=69/20) dou of roughly husked rice.
"""

from fractions import Fraction

# 粟二斗三升
粟斗 = 2
粟升 = 3

# Convert to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求糲飯，三之
糲飯 = 3 * 粟

# 二而一
a = Fraction(糲飯, 20) # 69/20 (in dou)#----- content ends here -----

"""
"""
