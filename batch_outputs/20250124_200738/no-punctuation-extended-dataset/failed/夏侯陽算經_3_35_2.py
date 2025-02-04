"""
今有糙米八千四百六十七斛五斗毎一斗五升碾熟米八升問米幾何
術曰先置糙米數以八因之十五升除之即得
答曰米 a斛
"""

#----- content starts here -----
"""
Suppose there are 8467 hu and 5 dou of rough rice. For every dou and 5 sheng, it produces 8 sheng of polished rice.
Question: how much polished rice is obtained?

The procedure says: First, place the number of rough rice. Multiply it by 8. Divide it by 15 sheng, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 糙米八千四百六十七斛五斗
糙米_斛 = 8467
糙米_斗 = 5

# Convert 糙米 to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
糙米_升 = (糙米_斛 * 10 + 糙米_斗) * 10

# 每一斗五升碾熟米八升
熟米率_分子 = 8  # Numerator for polished rice yield
熟米率_分母 = 15  # Denominator for polished rice yield

# 先置糙米數，以八因之
熟米_升 = 糙米_升 * 熟米率_分子

# 十五升除之，即得
熟米_斛 = Fraction(熟米_升, 熟米率_分母 * 10)  # Convert back to hu (1 hu = 100 sheng)

a = 熟米_斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4516, Actual: 45160"""
