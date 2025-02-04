"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
術曰：以粟求大䵂，二十七之，二十五而一。
荅曰：為大䵂 a(=1323/125)斗 。
"""

"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into daqu (a type of fermented grain product).
Question: how much daqu does one obtain?

The procedure says: when seeking daqu from millet, multiply by 27 and divide by 25.

The answer says: *a*(=1323/125) dou of daqu.
"""

from fractions import Fraction

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert 升 to 斗 (10 升 = 1 斗)
粟 = 粟斗 + Fraction(粟升, 10)

# 以粟求大䵂，二十七之
大䵂 = 27 * 粟

# 二十五而一
a = Fraction(大䵂, 25) # 1323/125

"""
"""
