"""
今有粟五斗五升欲為飧問得幾何
術曰以粟求飧九之五而一
荅曰為飧 a斗 
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 5 sheng of millet. It is desired to turn it into cooked millet (suan).
Question: how much cooked millet does one obtain?

The procedure says: when seeking cooked millet from millet, multiply by 9 and divide by 5.

The answer says: it makes *a* dou of cooked millet.
"""

# 粟五斗五升
粟斗 = 5
粟升 = 5

# Convert to total sheng (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求飧，九之
飧 = 9 * 粟總升

# 五而一
飧總升 = Fraction(飧, 5)

# Convert back to dou and sheng
飧斗 =飧總升 // 10
飧升 =飧總升 % 10

a = Fraction(飧總升, 10)  # Final answer in dou#----- content ends here -----

"""
"""
