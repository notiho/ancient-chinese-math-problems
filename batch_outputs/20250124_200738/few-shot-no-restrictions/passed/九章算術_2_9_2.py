"""
今有粟九斗八升，欲為御飯。問︰得幾何？
術曰：以粟求御飯，二十一之，二十五而一。
荅曰：為御飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into prepared rice (御飯).
Question: how much prepared rice is obtained?

The procedure says: When seeking prepared rice using millet, multiply by 21 and divide by 25.

The answer says: it makes *a* dou of prepared rice.
"""

from fractions import Fraction

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = (粟斗 * 10) + 粟升

# 以粟求御飯，二十一之
御飯升 = 21 * 粟總升

# 二十五而一
御飯總升 = Fraction(御飯升, 25)

# Convert back to dou and sheng
御飯斗 = 御飯總升 // 10  # Integer part is dou
御飯升 = 御飯總升 % 10   # Remainder is sheng

# Final result
a = Fraction(御飯斗) + Fraction(御飯升, 10)
a  # Answer in dou#----- content ends here -----

"""
"""
