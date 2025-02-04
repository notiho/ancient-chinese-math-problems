"""
今有粟七斗九升，欲為御米。問︰得幾何？
術曰：以粟求御米，二十一之，五十而一。
荅曰：為御米 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 7 dou and 9 sheng of unhusked millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The procedure says: when seeking polished rice from unhusked millet, multiply by 21 and divide by 50.

The answer says: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟七斗九升
粟斗 = 7
粟升 = 9

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = 粟斗 * 10 + 粟升

# 以粟求御米，二十一之
御米 = 21 * 粟總升

# 五十而一
御米斗 = Fraction(御米, 50)

# Convert back to 斗
a = 御米斗
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 1659/50"""
