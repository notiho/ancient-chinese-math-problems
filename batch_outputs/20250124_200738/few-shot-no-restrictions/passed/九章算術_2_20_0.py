"""
今有粺米二斗，欲為粟。問︰得幾何？
術曰：以粺米求粟，五十之，二十七而一。
荅曰：為粟 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou of polished rice (粺米). It is desired to convert it back into unhusked millet (粟).
Question: how much unhusked millet does it make?

The procedure says: When seeking unhusked millet using polished rice, multiply by 50 and divide by 27.

The answer says: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 粺米二斗
粺米 = 2

# 以粺米求粟，五十之
粟 = 50 * 粺米

# 二十七而一
a = Fraction(粟, 27)

# Output the result
a#----- content ends here -----

"""
"""
