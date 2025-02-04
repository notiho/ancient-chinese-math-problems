"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does one obtain?

The procedure says: When seeking cooked rice from millet, multiply by 24 and divide by 25.

The answer says: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 粟八斗六升
粟斗 = 8
粟升 = 6

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求鑿飯，二十四之
鑿飯升 = 24 * 粟總升

# 二十五而一
鑿飯 = Fraction(鑿飯升, 25)

# Convert back to dou and sheng
鑿飯斗 = 鑿飯 // 10  # Whole dou
鑿飯升 = 鑿飯 % 10   # Remaining sheng

a = f"{鑿飯斗}斗 {鑿飯升}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: 8斗 64/25升"""
