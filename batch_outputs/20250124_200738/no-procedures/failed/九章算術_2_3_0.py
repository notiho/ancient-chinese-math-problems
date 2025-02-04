"""
今有粟七斗九升，欲為御米。問︰得幾何？
荅曰：為御米 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou and 9 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice is obtained?

Answer: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟七斗九升
粟_斗 = 7
粟_升 = 9

# Convert everything to sheng (1 dou = 10 sheng)
粟_總升 = 粟_斗 * 10 + 粟_升

# Polished rice is obtained by multiplying the total millet by 2/3
御米_總升 = Fraction(2, 3) * 粟_總升

# Convert back to dou and sheng
御米_斗 = 御米_總升 // 10  # Whole number of dou
御米_升 = 御米_總升 % 10   # Remaining sheng

# Final result
a = Fraction(御米_斗) + Fraction(御米_升, 10)  # Represent as dou

a  # Output the result in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 79/15"""
