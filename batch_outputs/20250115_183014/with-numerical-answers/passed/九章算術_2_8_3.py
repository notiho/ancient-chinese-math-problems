"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a(=1032/125)斗 。
"""

"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

The procedure says: when seeking cooked rice from millet, multiply by 24 and divide by 25.

The answer says: it makes *a*(=1032/125) dou of cooked rice.
"""

# 粟八斗六升
粟斗 = 8
粟升 = 6

# Convert to total sheng (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求鑿飯，二十四之
鑿飯升 = 24 * 粟總升

# 二十五而一
鑿飯斗 = Fraction(鑿飯升, 25 * 10)  # Convert back to dou (divide by 10 for sheng to dou)

a = 鑿飯斗  # 1032/125 dou
"""
"""
