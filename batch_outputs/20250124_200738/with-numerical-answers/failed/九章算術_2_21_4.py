"""
今有鑿米三斗、少半升，欲為粟。問︰得幾何？
術曰：以鑿米求粟，二十五之，十二而一。
荅曰：為粟 a(=455/72)斗 。
"""

#----- content starts here -----
"""
Suppose there is 3 dou and half a sheng of polished rice. It is desired to turn it into unhusked millet.
Question: how much unhusked millet does it make?

The procedure says: when seeking unhusked millet using polished rice, multiply by 25 and divide by 12.

Answer: it makes *a*(=455/72) dou of unhusked millet.
"""

from fractions import Fraction

# 鑿米三斗、少半升
鑿米 = 3 + Fraction(1, 20)  # 3 dou and half a sheng (1 dou = 10 sheng)

# 以鑿米求粟，二十五之
粟 = 25 * 鑿米

# 十二而一
a = Fraction(粟, 12)  # 455/72 dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 455/72, Actual: 305/48"""
