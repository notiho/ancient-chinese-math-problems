"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
荅曰：為粺飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 3 dou and 6 sheng of millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The answer says: it makes *a* dou of polished rice.
"""

from fractions import Fraction

# 粟三斗六升
粟 = 3 + Fraction(6, 10)  # Convert 6 sheng to dou (1 dou = 10 sheng)

# Polished rice is obtained by multiplying millet by 2/3
a = 粟 * Fraction(2, 3)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 486/125, Actual: 12/5"""
