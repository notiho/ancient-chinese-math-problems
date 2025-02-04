"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
荅曰：為鑿飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 8 dou and 6 sheng of millet. It is desired to turn it into cooked rice.
Question: how much cooked rice does it make?

Answer: it makes *a* dou of cooked rice.
"""

from fractions import Fraction

# 粟八斗六升
粟_斗 = 8
粟_升 = 6

# Convert everything to sheng (1 dou = 10 sheng)
粟_總升 = 粟_斗 * 10 + 粟_升

# Cooked rice is obtained by multiplying millet by 2/3
鑿飯_總升 = Fraction(2, 3) * 粟_總升

# Convert back to dou and sheng
a_斗 = 鑿飯_總升 // 10  # Whole dou
a_升 = 鑿飯_總升 % 10   # Remaining sheng

# Final result
a = Fraction(a_斗) + Fraction(a_升, 10)  # Total in dou

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: 86/15"""
