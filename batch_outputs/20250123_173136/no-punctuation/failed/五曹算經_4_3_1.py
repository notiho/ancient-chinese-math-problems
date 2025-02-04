"""
今有粟九百斛斛别加二斗五升問加㡬何
術曰列九百斛以二斗五升乘之即得
答曰 a斛 
"""

"""
Suppose there are 900 hu of millet. For each hu, an additional 2 dou and 5 sheng are added.
Question: how much is added in total?

The procedure says: Place the 900 hu and multiply it by 2 dou and 5 sheng. The result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900

# 每斛加二斗五升
# Convert 2斗5升 to hu (1斗 = 10升, 1升 = 1/100斛)
每斛加 = 2 + Fraction(5, 10)

# 以二斗五升乘之
總加 = 粟 * 每斛加

# 答案
a = 總加
"""
Variable 'a' has wrong value. Expected: 225, Actual: 2250"""
