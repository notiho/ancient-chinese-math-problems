"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
荅曰：為糲飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 3 sheng of millet. It is desired to turn it into roughly husked rice.
Question: how much roughly husked rice does one obtain?

Answer: it makes *a* dou.
"""

from fractions import Fraction

# 粟二斗三升
粟 = 2 * 10 + 3  # Convert to sheng (1 dou = 10 sheng)

# To convert millet into husked rice, multiply by 3/5
糲飯 = Fraction(3 * 粟, 5)

# Convert back to dou
a = Fraction(糲飯, 10)  # 1 dou = 10 sheng

# Output result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 69/20, Actual: 69/50"""
