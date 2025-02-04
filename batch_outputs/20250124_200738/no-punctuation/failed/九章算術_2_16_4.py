"""
今有粟五斗五升欲為飧問得幾何
術曰以粟求飧九之五而一
荅曰為飧 a斗 
"""

#----- content starts here -----
"""
Suppose there are 5 dou and 5 sheng of millet. It is desired to turn it into cooked millet (food).
Question: how much cooked millet does one obtain?

The procedure says: when seeking cooked millet from millet, multiply by 9 and divide by 5.

The answer says: it makes *a* dou of cooked millet.
"""

from fractions import Fraction

# 粟五斗五升
粟斗 = 5
粟升 = 5

# Convert everything to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求飧，九之
飧 = 9 * 粟

# 五而一
a = Fraction(飧, 5)

# Convert back to 斗 (1 斗 = 10 升)
a斗 = a // 10  # Whole dou
a升 = a % 10   # Remaining sheng

a斗, a升#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 99/10, Actual: 99"""
