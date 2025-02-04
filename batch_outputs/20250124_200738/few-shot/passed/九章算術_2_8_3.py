"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice is obtained?

The procedure says: When seeking cooked rice from millet, multiply by 24, and divide by 25.

Answer: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 粟八斗六升
粟斗 = 8
粟升 = 6

# Convert 粟 to total 升 (1 斗 = 10 升)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求鑿飯，二十四之
鑿飯升 = 24 * 粟總升

# 二十五而一
鑿飯斗 = Fraction(鑿飯升, 25 * 10)  # Convert back to dou (1 斗 = 10 升)

a = 鑿飯斗#----- content ends here -----

"""
"""
