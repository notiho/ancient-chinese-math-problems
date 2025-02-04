"""
今有粟七斗九升，欲為御米。問︰得幾何？
術曰：以粟求御米，二十一之，五十而一。
荅曰：為御米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 9 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does it make?

The procedure says: When seeking polished rice from millet, multiply by 21 and divide by 50.

Answer: it makes *a* dou of polished rice.
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

# Convert back to 斗 and 升
a斗 = 御米斗 // 10  # Whole number of 斗
a升 = 御米斗 % 10   # Remaining 升

a = f"{a斗}斗 {a升}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 3斗 159/50升"""
