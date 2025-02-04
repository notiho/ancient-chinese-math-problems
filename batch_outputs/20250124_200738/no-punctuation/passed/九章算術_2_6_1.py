"""
今有粟二斗三升欲為糲飯問得幾何
術曰以粟求糲飯三之二而一
荅曰為糲飯 a斗 
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 3 sheng of millet. It is desired to turn it into roughly husked rice.
Question: how much roughly husked rice does one obtain?

The procedure says: when seeking roughly husked rice using millet, multiply by 3 and divide by 2.

The answer says: it makes *a* dou of roughly husked rice.
"""

# 粟二斗三升
粟 = 2 * 10 + 3  # Convert to sheng (1 dou = 10 sheng)

# 以粟求糲飯，三之
糲飯 = 3 * 粟

# 二而一
a = Fraction(糲飯, 2) / 10  # Convert back to dou

a#----- content ends here -----

"""
"""
