"""
今有粟九斗八升，欲為御飯。問︰得幾何？
術曰：以粟求御飯，二十一之，二十五而一。
荅曰：為御飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

The procedure says: When seeking cooked rice using millet, multiply by 21 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求御飯，二十一之
御飯升 = 21 * 粟總升

# 二十五而一
御飯斗 = Fraction(御飯升, 25 * 10)  # Convert back to 斗 (1 斗 = 10 升)

a = 御飯斗#----- content ends here -----

"""
"""
