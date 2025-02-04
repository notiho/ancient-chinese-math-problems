"""
今有粟五斗五升欲為飧問得幾何
術曰以粟求飧九之五而一
荅曰為飧 a斗 
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 5 sheng of millet. It is desired to turn it into cooked millet (fan).
Question: how much cooked millet does one obtain?

The procedure says: when seeking cooked millet using millet, multiply by 9 and divide by 5.

The answer says: it makes *a* dou of cooked millet.
"""

from fractions import Fraction

# 粟五斗五升
粟斗 = 5
粟升 = 5

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求飧，九之
飧升 = 9 * 粟總升

# 五而一
飧總升 = Fraction(飧升, 5)

# Convert back to 斗 (1 斗 = 10 升)
飧斗 = 飧總升 // 10  # Whole dou
飧升 = 飧總升 % 10   # Remaining sheng

a = Fraction(飧總升, 10)  # Represent the result as dou

# The result is in dou (a斗).#----- content ends here -----

"""
"""
