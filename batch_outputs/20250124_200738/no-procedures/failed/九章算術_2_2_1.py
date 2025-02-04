"""
今有粟四斗五升，欲為鑿米。問︰得幾何？
荅曰：為鑿米 a斗 。
"""

#----- content starts here -----
"""
Suppose there is 4 dou and 5 sheng of unhusked millet. It is desired to turn it into polished rice.
Question: how much polished rice does one obtain?

The answer says: *a* dou.
"""

from fractions import Fraction

# 粟四斗五升
粟 = 4 + Fraction(5, 10)  # Convert 4 dou 5 sheng into dou (1 dou = 10 sheng)

# Polished rice is obtained by multiplying by 2/3
a = 粟 * Fraction(2, 3)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 3"""
