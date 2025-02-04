"""
今有糙米八千四百六十七斛五斗毎一斗五升碾熟米八升問米幾何
術曰先置糙米數以八因之十五升除之即得
答曰米 a斛
"""

"""
Suppose there are 8467 hu and 5 dou of rough rice. For every dou and 5 sheng of rough rice, 8 sheng of polished rice is obtained.
Question: how much polished rice is there in total?

The procedure says: First, place the amount of rough rice. Multiply it by 8. Divide it by 15 sheng, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 糙米數：八千四百六十七斛五斗
糙米斛 = 8467
糙米斗 = 5

# Convert 糙米 to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
糙米升 = (糙米斛 * 10 + 糙米斗) * 10

# 每一斗五升碾熟米八升
粗米轉熟米率 = Fraction(8, 15)

# 以八因之，十五升除之
熟米升 = 糙米升 * 粗米轉熟米率

# Convert 熟米升 back to hu (1 hu = 100 sheng)
a = Fraction(熟米升, 100)  # Answer in hu
"""
"""
