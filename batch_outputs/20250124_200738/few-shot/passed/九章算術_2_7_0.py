"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 3 dou and 6 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice is obtained?

The procedure says: When seeking polished rice using millet, multiply by 27 and divide by 25.

The answer says: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟三斗六升
粟斗 = 3
粟升 = 6

# Convert everything to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求粺飯，二十七之
粺飯 = 27 * 粟

# 二十五而一
粺飯 = Fraction(粺飯, 25)

# Convert back to 斗 (1 斗 = 10 升)
a = Fraction(粺飯, 10)  # Result in dou#----- content ends here -----

"""
"""
