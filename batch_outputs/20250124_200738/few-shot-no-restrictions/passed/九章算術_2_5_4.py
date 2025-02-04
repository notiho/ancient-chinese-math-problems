"""
今有粟九斗八升，欲為大䵂。問︰得幾何？
術曰：以粟求大䵂，二十七之，二十五而一。
荅曰：為大䵂 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into daqu (a type of fermented grain product).
Question: how much daqu is obtained?

The procedure says: When seeking daqu from millet, multiply by 27 and divide by 25.

Answer: it makes *a* dou of daqu.
"""

from fractions import Fraction

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求大䵂，二十七之
大䵂 = 27 * 粟總升

# 二十五而一
大䵂斗 = Fraction(大䵂, 25) / 10  # Convert back to dou

a = 大䵂斗
#----- content ends here -----

"""
"""
