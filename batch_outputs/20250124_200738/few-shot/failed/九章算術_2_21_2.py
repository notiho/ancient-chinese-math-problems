"""
今有鑿米三斗、少半升，欲為粟。問︰得幾何？
術曰：以鑿米求粟，二十五之，十二而一。
荅曰：為粟 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 3 dou and half a sheng of polished rice. It is desired to convert it back to unhusked millet.
Question: how much unhusked millet does it make?

The procedure says: To seek unhusked millet from polished rice, multiply by 25 and divide by 12.

Answer: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 鑿米三斗、少半升
鑿米 = 3 + Fraction(1, 2) / 10  # Convert half a sheng to dou (1 dou = 10 sheng)

# 以鑿米求粟，二十五之
粟 = 25 * 鑿米

# 十二而一
a = Fraction(粟, 12)  # Result in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 455/72, Actual: 305/48"""
