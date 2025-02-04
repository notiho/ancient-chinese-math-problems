"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
荅曰：為鑿飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 8 dou and 6 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The answer says: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟八斗六升
粟_斗 = 8
粟_升 = 6

# Convert everything to sheng (1 dou = 10 sheng)
粟_總升 = 粟_斗 * 10 + 粟_升

# Polished rice is obtained by multiplying millet by 2/3
鑿飯_總升 = Fraction(2, 3) * 粟_總升

# Convert back to dou and sheng
a_斗 = 鑿飯_總升 // 10  # Whole dou
a_升 = 鑿飯_總升 % 10   # Remaining sheng

# Final result
a = Fraction(a_斗) + Fraction(a_升, 10)

a  # Answer in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: 86/15"""
