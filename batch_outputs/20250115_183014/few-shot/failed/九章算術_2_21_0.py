"""
今有鑿米三斗、少半升，欲為粟。問︰得幾何？
術曰：以鑿米求粟，二十五之，十三而一。
荅曰：為粟 a斗 。
"""

"""
Suppose there is 3 dou and half a sheng of polished rice. It is desired to turn it into unhusked millet.
Question: how much unhusked millet does it make?

The procedure says: when seeking unhusked millet using polished rice, multiply by 25 and divide by 13.

The answer says: it makes *a* dou of unhusked millet.
"""

# 鑿米三斗、少半升
鑿米 = 3 + Fraction(1, 2)  # Convert to dou (3 dou and half a sheng)

# 以鑿米求粟，二十五之
粟 = 25 * 鑿米

# 十三而一
a = Fraction(粟, 13)  # Result in dou
"""
Variable 'a' has wrong value. Expected: 455/72, Actual: 175/26"""
