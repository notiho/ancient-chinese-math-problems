"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
荅曰：為糲飯 a斗 。
"""

"""
Suppose there is 2 dou and 3 sheng of millet. It is desired to turn it into roughly husked rice.
Question: how much husked rice does one obtain?

The answer says: it makes *a* dou of husked rice.
"""

from fractions import Fraction

# 粟二斗三升
粟 = 2 + Fraction(3, 10)  # Convert 2 dou and 3 sheng into dou (1 dou = 10 sheng)

# Multiply by 3/5 to get husked rice
a = 粟 * Fraction(3, 5)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 69/20, Actual: 69/50"""
