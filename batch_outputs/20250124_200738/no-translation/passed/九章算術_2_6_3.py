"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a斗 。
"""

#----- content starts here -----

# 粟二斗三升
粟斗 = 2
粟升 = 3

# Convert to 升 (1斗 = 10升)
粟 = (粟斗 * 10) + 粟升

# 以粟求糲飯，三之
糲飯 = 3 * 粟

# 二而一
a = Fraction(糲飯, 2) / 10  # Convert back to 斗

#----- content ends here -----

"""
"""
