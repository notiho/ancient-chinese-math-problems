"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
術曰：以粟求糲飯，三之，二而一。
荅曰：為糲飯 a斗 。
"""

#----- content starts here -----

# 粟二斗三升
粟斗 = 2
粟升 = 3

# Convert 粟 to 升 (1斗 = 10升)
粟 = 10 * 粟斗 + 粟升

# 以粟求糲飯，三之
糲飯 = 3 * 粟

# 二而一
a = Fraction(糲飯, 2) / 10  # Convert back to 斗

# Final result in 斗
a#----- content ends here -----

"""
"""
