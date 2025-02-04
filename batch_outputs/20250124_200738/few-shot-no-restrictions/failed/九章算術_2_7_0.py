"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 3 dou and 6 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice is obtained?

The procedure says: When seeking polished rice from millet, multiply by 27 and divide by 25.

Answer: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟三斗六升
粟斗 = 3
粟升 = 6

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求粺飯，二十七之
粺飯升 = 27 * 粟總升

# 二十五而一
粺飯 = Fraction(粺飯升, 25)

# Convert back to dou and sheng
粺飯斗 = 粺飯 // 10  # Whole dou
粺飯升 = 粺飯 % 10   # Remaining sheng

a = f"{粺飯斗}斗 {粺飯升}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 486/125, Actual: 3斗 222/25升"""
