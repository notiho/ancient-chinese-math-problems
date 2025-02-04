"""
今有粟二斗三升，欲為糲飯。問︰得幾何？
荅曰：為糲飯 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 2 dou and 3 sheng of millet. It is desired to turn it into roughly husked rice.
Question: how much husked rice does it produce?

Answer: it makes *a* dou of husked rice.
"""

from fractions import Fraction

# 粟二斗三升
粟 = 2 * 10 + 3  # Convert to sheng (1 dou = 10 sheng)

# To convert millet to husked rice, multiply by 3/5
糲飯 = Fraction(3, 5) * 粟

# Convert back to dou and sheng
a_dou = 糲飯 // 10  # Whole dou
a_sheng = 糲飯 % 10  # Remaining sheng

# Final result
a = f"{a_dou}斗 {a_sheng}升"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 69/20, Actual: 1斗 19/5升"""
