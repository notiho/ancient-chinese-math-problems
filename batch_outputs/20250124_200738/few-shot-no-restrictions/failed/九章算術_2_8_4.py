"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it yield?

The procedure says: When seeking cooked rice from millet, multiply by 24 and divide by 25.

Answer: it yields *a* dou of cooked rice.
"""

from fractions import Fraction

# 粟八斗六升
粟_斗 = 8
粟_升 = 6

# Convert everything to 升 (1 斗 = 10 升)
粟 = 10 * 粟_斗 + 粟_升  # Total 粟 in 升

# 以粟求鑿飯，二十四之
鑿飯 = 24 * 粟

# 二十五而一
a = Fraction(鑿飯, 25)

# Convert back to dou and sheng
a_斗 = a // 10  # Whole dou
a_升 = a % 10   # Remaining sheng

a_斗, a_升  # Answer in dou and sheng#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: 2064/25"""
