"""
今有粟七斗九升，欲為御米。問︰得幾何？
術曰：以粟求御米，二十一之，五十而一。
荅曰：為御米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 9 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The procedure says: when seeking polished rice from millet, multiply by 21 and divide by 50.

The answer says: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟七斗九升
粟斗 = 7
粟升 = 9

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求御米，二十一之
御米 = 21 * 粟總升

# 五十而一
御米斗 = Fraction(御米, 50)

# Convert back to dou and sheng
a斗 = 御米斗 // 10  # Whole dou
a升 = 御米斗 % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 3斗 159/50升"""
