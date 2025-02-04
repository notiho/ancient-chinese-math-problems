"""
今有粟四斗五升，欲為鑿米。問︰得幾何？
術曰：以粟求鑿米，十二之，二十五而一。
荅曰：為鑿米 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 4 dou and 5 sheng of unhusked millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The procedure says: When seeking polished rice from unhusked millet, multiply by 12 and divide by 25.

The answer says: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟四斗五升
粟斗 = 4
粟升 = 5

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求鑿米，十二之
鑿米 = 12 * 粟總升

# 二十五而一
鑿米 = Fraction(鑿米, 25)

# Convert back to dou and sheng
鑿米斗 = 鑿米 // 10  # Whole dou
鑿米升 = 鑿米 % 10   # Remaining sheng

a = Fraction(鑿米, 10)  # Final answer in dou

# Output
a#----- content ends here -----

"""
"""
