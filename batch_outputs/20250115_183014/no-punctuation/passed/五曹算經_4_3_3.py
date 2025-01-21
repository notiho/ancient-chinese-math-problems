"""
今有粟九百斛斛别加二斗五升問加㡬何
術曰列九百斛以二斗五升乘之即得
答曰 a斛 
"""

"""
Suppose there are 900 hu of millet. Each hu is increased by 2 dou and 5 sheng.
Question: how much is the total increase?

The procedure says: Place the 900 hu and multiply it by 2 dou and 5 sheng. This gives the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900

# 斛别加二斗五升
加斗 = 2
加升 = 5

# Convert 2斗5升 to 斛 (1斗 = 10升, 1斛 = 10斗 = 100升)
加量 = Fraction(加斗 * 10 + 加升, 100)  # Convert to hu

# 以九百斛乘之
總加量 = 粟 * 加量

a = 總加量
"""
"""
