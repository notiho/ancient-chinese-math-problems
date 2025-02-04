"""
今有粟八斗六升欲為鑿飯問得幾何
術曰以粟求鑿飯二十四之二十五而一
荅曰為鑿飯 a斗 
"""

"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

The procedure says: When seeking cooked rice using millet, multiply by 24 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

# 粟八斗六升
粟斗 = 8
粟升 = 6

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求鑿飯，二十四之
鑿飯 = 24 * 粟總升

# 二十五而一
鑿飯升 = Fraction(鑿飯, 25)

# Convert back to 斗 (1 斗 = 10 升)
a斗 = Fraction(鑿飯升, 10)  # This gives the result in dou

a = a斗
"""
"""
