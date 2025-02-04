"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a斗 。
"""

"""
Suppose there is 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

The procedure says: when seeking cooked rice using millet, multiply by 24 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 粟八斗六升
粟斗 = 8
粟升 = 6

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求鑿飯，二十四之
鑿飯升 = 24 * 粟總升

# 二十五而一
鑿飯斗 = Fraction(鑿飯升, 25 * 10)  # Convert back to 斗

a = 鑿飯斗
"""
"""
