"""
今有糙米八千四百六十七斛五斗毎一斗五升碾熟米八升問米幾何
術曰先置糙米數以八因之十五升除之即得
答曰米 a斛
"""

"""
Suppose there are 8467 hu and 5 dou of rough rice. For every dou and 5 sheng, 8 sheng of polished rice is obtained.
Question: how much polished rice is there?

The procedure says: First, place the amount of rough rice. Multiply it by 8. Then divide it by 15 sheng, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 糙米八千四百六十七斛五斗
糙米斛 = 8467
糙米斗 = 5

# Convert 糙米 to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
糙米升 = (糙米斛 * 10 + 糙米斗) * 10

# 每一斗五升碾熟米八升
# 1 dou 5 sheng = 15 sheng produces 8 sheng of polished rice
粗米因數 = 8
粗米除數 = 15

# 以八因之
熟米升 = 糙米升 * 粗米因數

# 十五升除之
熟米升 = Fraction(熟米升, 粗米除數)

# Convert polished rice back to hu (1 hu = 100 sheng)
a = Fraction(熟米升, 100)  # Final result in hu
"""
"""
