"""
今有粟二斗一升，欲為粺米。問︰得幾何？
術曰：以粟求粺米，二十七之，五十而一。
荅曰：為粺米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 1 sheng of unhusked millet. It is desired to turn it into polished millet.
Question: how much polished millet does one obtain?

The procedure says: when seeking polished millet from unhusked millet, multiply by 27 and divide by 50.

The answer says: it makes *a* dou of polished millet.
"""

from fractions import Fraction

# 粟二斗一升
粟斗 = 2
粟升 = 1

# Convert everything to 升 (1 斗 = 10 升)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求粺米，二十七之
粺米 = 27 * 粟總升

# 五十而一
粺米結果 = Fraction(粺米, 50)

# Convert back to 斗 and 升
粺米斗 = 粺米結果 // 10  # Whole number of 斗
粺米升 = 粺米結果 % 10   # Remaining 升

a = Fraction(粺米結果, 10)  # Final result in 斗
#----- content ends here -----

"""
"""
