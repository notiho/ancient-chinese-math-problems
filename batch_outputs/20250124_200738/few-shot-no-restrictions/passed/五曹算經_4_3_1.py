"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 900 hu of millet, and each hu is increased by 2 dou and 5 sheng.
Question: how much is the total increase?

The procedure says: Multiply 900 hu by 2 dou and 5 sheng, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 粟九百斛
粟 = 900  # in hu

# 每斛加二斗五升
加斗 = 2  # dou
加升 = 5  # sheng

# Convert dou and sheng to hu (1 hu = 10 dou, 1 dou = 10 sheng)
加量 = Fraction(加斗 * 10 + 加升, 100)  # Total increase per hu in hu

# 列九百斛以二斗五升乘之即得
總加量 = 粟 * 加量

# 答
a = 總加量
#----- content ends here -----

"""
"""
