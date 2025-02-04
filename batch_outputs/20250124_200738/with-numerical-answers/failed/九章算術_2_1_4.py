"""
今有粟二斗一升，欲為粺米。問︰得幾何？
術曰：以粟求粺米，二十七之，五十而一。
荅曰：為粺米 a(=567/500)斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 1 sheng of unhusked millet. It is desired to turn it into polished millet.
Question: how much polished millet does one obtain?

The procedure says: when seeking polished millet with unhusked millet, multiply by 27 and divide by 50.

The answer says: *a*(=567/500) dou of polished millet.
"""

from fractions import Fraction

# 粟二斗一升
粟斗 = 2
粟升 = 1

# Convert to total sheng (1 dou = 10 sheng)
粟總升 = 10 * 粟斗 + 粟升

# 以粟求粺米，二十七之
粺米升 = 27 * 粟總升

# 五十而一
粺米斗 = Fraction(粺米升, 50)

# Convert back to dou
a =粺米斗 # 567/500#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 567/50"""
