"""
今有粟九斗八升，欲為御飯。問︰得幾何？
術曰：以粟求御飯，二十一之，二十五而一。
荅曰：為御飯 a(=1029/125)斗 。
"""

"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice is obtained?

The procedure says: when seeking cooked rice from millet, multiply by 21 and divide by 25.

The answer says: *a*(=1029/125) dou of cooked rice.
"""

from fractions import Fraction

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert 粟 to total 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求御飯，二十一之
御飯 = 21 * 粟

# 二十五而一
a = Fraction(御飯, 25) / 10  # Convert back to dou (divide by 10升 per斗)

# a = 1029/125 dou
"""
"""
