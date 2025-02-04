"""
今有粟九斗八升，欲為御飯。問︰得幾何？
術曰：以粟求御飯，二十一之，二十五而一。
荅曰：為御飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does one obtain?

The procedure says: when seeking cooked rice from millet, multiply by 21 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求御飯，二十一之
御飯升 = 21 * 粟總升

# 二十五而一
御飯斗 = Fraction(御飯升, 25)

# Convert back to dou and sheng
a斗 = 御飯斗 // 10  # Whole dou
a升 = 御飯斗 % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1029/125, Actual: 8斗 58/25升"""
