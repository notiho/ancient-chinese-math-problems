"""
今有粟二斗三升欲為糲飯問得幾何
術曰以粟求糲飯三之二而一
荅曰為糲飯 a斗 
"""

"""
Suppose there are 2 dou and 3 sheng of millet. It is desired to turn it into roughly husked rice.
Question: how much roughly husked rice does one obtain?

The procedure says: when seeking roughly husked rice from millet, multiply by 3 and divide by 2.

The answer says: it makes *a* dou of roughly husked rice.
"""

# 粟二斗三升
粟斗 = 2
粟升 = 3

# Convert to 升 (1 斗 = 10 升)
粟 = (粟斗 * 10) + 粟升

# 以粟求糲飯，三之
糲飯 = 3 * 粟

# 二而一
a = Fraction(糲飯, 2)

# Convert back to dou and sheng if needed
糲飯斗 = a // 10  # Whole dou
糲飯升 = a % 10   # Remaining sheng

a斗 = f"{糲飯斗}斗 {糲飯升}升" if 糲飯升 != 0 else f"{糲飯斗}斗"

"""
Variable 'a' has wrong value. Expected: 69/20, Actual: 69/2"""
