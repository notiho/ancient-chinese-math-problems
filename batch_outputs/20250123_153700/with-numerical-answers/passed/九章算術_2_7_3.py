"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a(=486/125)斗 。
"""

"""
Suppose there are 3 dou and 6 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The procedure says: when seeking polished rice with millet, multiply by 27 and divide by 25.

The answer says: it makes *a*(=486/125) dou of polished rice.
"""

from fractions import Fraction

# 粟三斗六升
粟斗 = 3
粟升 = 6

# Convert to total dou (1 dou = 10 sheng)
粟 = 粟斗 + Fraction(粟升, 10)

# 以粟求粺飯，二十七之
粺飯 = 27 * 粟

# 二十五而一
a = Fraction(粺飯, 25) # 486/125 dou
"""
"""
