"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
荅曰：為粺飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 3 dou and 6 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

Answer: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟三斗六升
粟斗 = 3
粟升 = 6

# Convert everything to sheng (1 dou = 10 sheng)
粟總升 = 粟斗 * 10 + 粟升

# Polished rice is obtained by multiplying by 2/3
粺飯總升 = Fraction(2, 3) * 粟總升

# Convert back to dou and sheng
粺飯斗 = 粺飯總升 // 10  # Whole dou
粺飯升 = 粺飯總升 % 10   # Remaining sheng

# Final result
a = Fraction(粺飯斗) + Fraction(粺飯升, 10)  # Represent as dou with fractional part if needed

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 486/125, Actual: 12/5"""
