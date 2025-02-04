"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a(=225)斛 。
"""

"""
Suppose there are 900 hu of millet, and for each hu, an additional 2 dou and 5 sheng are added.
Question: how much is the total addition?

The procedure says: Place the 900 hu and multiply it by 2 dou and 5 sheng to obtain the result.

Answer: *a*(=225) hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900

# 斛别加二斗五升
加斗 = 2
加升 = 5

# Convert 2斗5升 to 斛 (1斗 = 10升, 1斛 = 10斗 = 100升)
加量 = Fraction(加斗 * 10 + 加升, 100)  # Convert to hu

# 以二斗五升乘之即得
a = 粟 * 加量  # 225 hu
"""
"""
