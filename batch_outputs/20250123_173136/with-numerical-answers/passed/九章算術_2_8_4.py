"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a(=1032/125)斗 。
"""

"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does one obtain?

The procedure says: when seeking cooked rice from millet, multiply by 24 and divide by 25.

The answer says: *a*(=1032/125) dou of cooked rice.
"""

from fractions import Fraction

# 粟八斗六升
粟斗 = 8
粟升 = 6

# Convert 升 to 斗 (10 升 = 1 斗)
粟 = 粟斗 + Fraction(粟升, 10)

# 以粟求鑿飯，二十四之
鑿飯 = 24 * 粟

# 二十五而一
a = Fraction(鑿飯, 25) # 1032/125
"""
"""
