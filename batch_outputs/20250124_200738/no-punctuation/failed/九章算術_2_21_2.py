"""
今有鑿米三斗少半升欲為粟問得幾何
術曰以鑿米求粟二十五之十三而一
荅曰為粟 a斗 
"""

#----- content starts here -----
"""
Suppose there are 3 dou and half a sheng of polished rice. It is desired to convert it into unhusked millet.
Question: how much unhusked millet does it make?

The procedure says: when seeking unhusked millet using polished rice, multiply by 25 and divide by 13.

The answer says: it makes *a* dou of unhusked millet.
"""

from fractions import Fraction

# 鑿米三斗少半升
鑿米 = 3 + Fraction(1, 2)  # Convert to dou, including the half sheng

# 以鑿米求粟，二十五之
粟 = 25 * 鑿米

# 十三而一
a = Fraction(粟, 13)  # Result in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 455/72, Actual: 175/26"""
