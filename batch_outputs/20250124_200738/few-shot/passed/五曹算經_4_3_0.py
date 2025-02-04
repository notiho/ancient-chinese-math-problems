"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 900 hu of millet, and each hu is increased by 2 dou and 5 sheng.
Question: how much is the total increase?

The procedure says: Place 900 hu and multiply it by 2 dou and 5 sheng to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900

# 斛别加二斗五升
加斗 = 2
加升 = 5

# Convert 2斗5升 to hu (1 hu = 10 dou, 1 dou = 10 sheng)
加量 = Fraction(加斗 * 10 + 加升, 100)

# 列九百斛以二斗五升乘之即得
a = 粟 * 加量#----- content ends here -----

"""
"""
