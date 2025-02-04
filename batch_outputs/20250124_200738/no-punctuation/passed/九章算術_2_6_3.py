"""
今有粟二斗三升欲為糲飯問得幾何
術曰以粟求糲飯三之二而一
荅曰為糲飯 a斗 
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 3 sheng of unhusked millet. It is desired to turn it into roughly husked rice.
Question: how much does one obtain?

The procedure says: when seeking roughly husked rice from unhusked millet, multiply by 3 and divide by 2.

The answer says: it makes *a* dou of roughly husked rice.
"""

# 粟二斗三升
粟斗 = 2
粟升 = 3

# Convert to 升 (1 dou = 10 sheng)
粟 = (粟斗 * 10) + 粟升

# 以粟求糲飯，三之
糲飯 = 3 * 粟

# 二而一
糲飯 = Fraction(糲飯, 2)

# Convert back to dou and sheng
a斗 = 糲飯 // 10  # Whole dou
a升 = 糲飯 % 10   # Remaining sheng

a = Fraction(a斗) + Fraction(a升, 10)  # Final result in dou
#----- content ends here -----

"""
"""
