"""
今有米二千五百六十七斛五斗其米麤欲再舂毎八升耗一升問合得熟米幾何
術曰置米數以七因八除得數返求米以八因七除
答曰熟米 a斛
"""

"""
Suppose there are 2567 hu and 5 dou of coarse rice. It is desired to mill it twice.
For every 8 sheng, 1 sheng is lost.
Question: how much polished rice is obtained in total?

The procedure says: Place the amount of rice. Multiply it by 7 and divide by 8 to get the result.
To reverse and seek the original rice, multiply by 8 and divide by 7.

Answer: *a* hu of polished rice.
"""

from fractions import Fraction

# 米二千五百六十七斛五斗
米_斛 = 2567
米_斗 = 5

# Convert everything to dou (1 hu = 10 dou)
總米 = 米_斛 * 10 + 米_斗

# 每八升耗一升 (7 parts remain out of 8)
# 以七因八除
熟米_斗 = Fraction(7, 8) * 總米

# Convert back to hu and dou (1 hu = 10 dou)
熟米_斛 = 熟米_斗 // 10
熟米_餘斗 = 熟米_斗 % 10

a = Fraction(熟米_斛) + Fraction(熟米_餘斗, 10)  # Final answer in hu
"""
"""
